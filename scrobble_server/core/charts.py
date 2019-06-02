from collections import namedtuple
from copy import deepcopy
import datetime
import json
from typing import Optional

TopListData = namedtuple(
    "TopListData", "category toplist, total_listens, max_listen_count, type"
)


class TopList:
    CATGEORIES = ["artists", "albums", "tracks", "listeners"]
    TIMESPANS = ["all", "year", "month", "week", "day"]

    def __init__(self, obj, category: str, timespan: str, date: datetime.date):
        assert category in self.CATGEORIES
        assert timespan in self.TIMESPANS

        self.obj = obj
        self.category = category
        self.timespan = timespan
        self.date = date

    def get(self) -> TopListData:
        # always return live data if timespan=day and date=today
        today = datetime.datetime.now(datetime.timezone.utc).date()
        if self.timespan == "day" and self.date == today:
            return self.live()

        cached = self.cached()
        if not cached:
            return self.live()
        else:
            return cached

    def cached(self) -> Optional[TopListData]:
        result = self.obj.charts.filter(
            category=self.category, timespan=self.timespan, date=self.date
        ).first()

        if not result:
            return None

        else:
            return TopListData(
                category=self.category,
                toplist=json.loads(result.toplist),
                total_listens=result.total_listens,
                max_listen_count=result.max_listen_count,
                type="cached",
            )

    def live(self) -> TopListData:
        if self.category == "artists":
            toplist = self.qs.top_artists()
        elif self.category == "albums":
            toplist = self.qs.top_albums()
        elif self.category == "tracks":
            toplist = self.qs.top_tracks()
        elif self.category == "listeners":
            toplist = self.qs.top_listeners()
        elif self.category == "all":
            toplist = self.qs.all()

        # max_listen_count is count of first element or zero for no elements
        if toplist.count() > 0:
            max_listen_count = toplist[0]["count"]
        else:
            max_listen_count = 0

        return TopListData(
            category=self.category,
            toplist=list(toplist),
            total_listens=toplist.count(),
            max_listen_count=max_listen_count,
            type="live",
        )

    @staticmethod
    def combine_results(one: TopListData, two: TopListData) -> TopListData:
        # make sure both results are from the same category
        assert one.category == two.category
        assert one.category in TopList.CATGEORIES

        # if one of them is empty, return the other
        if one.total_listens == 0:
            return two
        if two.total_listens == 0:
            return one

        id_field = "{}__id".format(one.category[:-1])

        # deepcopy both lists so we don't modify original data
        # toplist1 = deepcopy(one.toplist)
        # toplist2 = deepcopy(two.toplist)

        # from the first toplist, create a dictionary with the values of
        # the id fields as key
        d = {x[id_field]: deepcopy(x) for x in one.toplist}

        # iterate over the second toplist
        for item in two.toplist:
            # see if the current item id already exists in the dictionary
            item_id = item[id_field]
            existing_item = d.get(item_id)

            # if the item doesn't exist, set current item in the dict
            if not existing_item:
                d[item_id] = deepcopy(item)
            # otherwise, add counts
            else:
                d[item_id]["count"] += item["count"]

        # create a sorted list from combined items
        items = sorted(
            d.values(),
            key=lambda x: (
                -x["count"],
                x.get("artist__name"),
                x.get("track__title"),
                x.get("album__title"),
            ),
        )

        # find out new type
        if one.type == two.type:
            type_ = one.type
        else:
            type_ = "hybrid"

        # return new TopListData with combined values
        return TopListData(
            category=one.category,
            toplist=items,
            total_listens=one.total_listens + two.total_listens,
            max_listen_count=items[0]["count"],
            type=type_,
        )

    @property
    def today_in_range(self) -> bool:
        today = datetime.datetime.now(datetime.timezone.utc).date()

        if self.timespan == "year":
            return today.year == self.date.year
        elif self.timespan == "month":
            return today.year == self.date.year and today.month == self.date.month
        elif self.timespan == "week":
            return self.date <= today < self.date + datetime.timedelta(weeks=1)
        elif self.timespan == "day":
            return today == self.date
        elif self.timespan == "all":
            return True

    @property
    def qs(self):
        if self.timespan == "all":
            return self.obj.scrobbles.all()
        elif self.timespan == "year":
            return self.obj.scrobbles.year(self.date)
        elif self.timespan == "month":
            return self.obj.scrobbles.month(self.date)
        elif self.timespan == "week":
            return self.obj.scrobbles.week(self.date)
        elif self.timespan == "day":
            return self.obj.scrobbles.day(self.date)
