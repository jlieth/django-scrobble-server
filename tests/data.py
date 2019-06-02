from copy import deepcopy
import datetime

from scrobble_server.core.charts import TopListData

top_artists = [
    {"artist__name": "Dancing Unquestioningly", "artist__id": 8, "count": 52},
    {"artist__name": "Stop Nobodies", "artist__id": 2, "count": 52},
    {"artist__name": "Lenient Fascinated Apparatus", "artist__id": 7, "count": 51},
    {"artist__name": "King Of All Memoirs", "artist__id": 4, "count": 35},
    {"artist__name": "Buckets For You", "artist__id": 9, "count": 15},
    {"artist__name": "Consequently Loud", "artist__id": 10, "count": 14},
    {"artist__name": "Lesser Paraphrase Variable", "artist__id": 6, "count": 14},
    {"artist__name": "Oblivious Hosts", "artist__id": 3, "count": 14},
    {"artist__name": "Bedeviling Instrument", "artist__id": 5, "count": 13},
    {"artist__name": "Pathetic Genius", "artist__id": 1, "count": 13},
]

top_artists_overall = deepcopy(top_artists)
for artist in top_artists_overall:
    artist["count"] *= 3

top_artists_2009 = deepcopy(top_artists)
for artist in top_artists_2009:
    artist["count"] *= 2

top_artists_2008 = [
    {"artist__name": "Stop Nobodies", "artist__id": 2, "count": 31},
    {"artist__name": "Dancing Unquestioningly", "artist__id": 8, "count": 29},
    {"artist__name": "Lenient Fascinated Apparatus", "artist__id": 7, "count": 22},
    {"artist__name": "King Of All Memoirs", "artist__id": 4, "count": 18},
    {"artist__name": "Lesser Paraphrase Variable", "artist__id": 6, "count": 10},
    {"artist__name": "Buckets For You", "artist__id": 9, "count": 6},
    {"artist__name": "Consequently Loud", "artist__id": 10, "count": 6},
    {"artist__name": "Pathetic Genius", "artist__id": 1, "count": 6},
    {"artist__name": "Bedeviling Instrument", "artist__id": 5, "count": 5},
    {"artist__name": "Oblivious Hosts", "artist__id": 3, "count": 4},
]

top_artists_2007 = [
    {"artist__name": "Lenient Fascinated Apparatus", "artist__id": 7, "count": 29},
    {"artist__name": "Dancing Unquestioningly", "artist__id": 8, "count": 23},
    {"artist__name": "Stop Nobodies", "artist__id": 2, "count": 21},
    {"artist__name": "King Of All Memoirs", "artist__id": 4, "count": 17},
    {"artist__name": "Oblivious Hosts", "artist__id": 3, "count": 10},
    {"artist__name": "Buckets For You", "artist__id": 9, "count": 9},
    {"artist__name": "Bedeviling Instrument", "artist__id": 5, "count": 8},
    {"artist__name": "Consequently Loud", "artist__id": 10, "count": 8},
    {"artist__name": "Pathetic Genius", "artist__id": 1, "count": 7},
    {"artist__name": "Lesser Paraphrase Variable", "artist__id": 6, "count": 4},
]

top_artists_2009_week_20 = [
    {"artist__name": "Lenient Fascinated Apparatus", "artist__id": 7, "count": 51},
    {"artist__name": "King Of All Memoirs", "artist__id": 4, "count": 31},
    {"artist__name": "Dancing Unquestioningly", "artist__id": 8, "count": 15},
    {"artist__name": "Stop Nobodies", "artist__id": 2, "count": 8},
    {"artist__name": "Lesser Paraphrase Variable", "artist__id": 6, "count": 7},
    {"artist__name": "Bedeviling Instrument", "artist__id": 5, "count": 6},
    {"artist__name": "Consequently Loud", "artist__id": 10, "count": 4},
    {"artist__name": "Buckets For You", "artist__id": 9, "count": 3},
    {"artist__name": "Pathetic Genius", "artist__id": 1, "count": 3},
    {"artist__name": "Oblivious Hosts", "artist__id": 3, "count": 2},
]

top_artists_2009_05_11 = [
    {"artist__name": "King Of All Memoirs", "artist__id": 4, "count": 15},
    {"artist__name": "Lesser Paraphrase Variable", "artist__id": 6, "count": 7},
    {"artist__name": "Buckets For You", "artist__id": 9, "count": 3},
    {"artist__name": "Dancing Unquestioningly", "artist__id": 8, "count": 3},
    {"artist__name": "Oblivious Hosts", "artist__id": 3, "count": 2},
    {"artist__name": "Pathetic Genius", "artist__id": 1, "count": 2},
    {"artist__name": "Bedeviling Instrument", "artist__id": 5, "count": 1},
]

top_albums = [
    {
        "artist__name": "Dancing Unquestioningly",
        "album__title": "Whispers Of Yesterday",
        "album__id": 9,
        "count": 52,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "album__title": "Lyrical And Things",
        "album__id": 7,
        "count": 51,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Dreaming Of Time",
        "album__id": 2,
        "count": 24,
    },
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "He Can Sing",
        "album__id": 8,
        "count": 19,
    },
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "So Do I",
        "album__id": 4,
        "count": 16,
    },
    {
        "artist__name": "Oblivious Hosts",
        "album__title": "Summer Of My Enemy",
        "album__id": 3,
        "count": 14,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "album__title": "A Way Of Never",
        "album__id": 5,
        "count": 13,
    },
    {
        "artist__name": "Pathetic Genius",
        "album__title": "Memories Of My Thoughts",
        "album__id": 1,
        "count": 13,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "Call Of His Imagination",
        "album__id": 11,
        "count": 11,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Sweet Dreams Tonight",
        "album__id": 13,
        "count": 11,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Dance For A Rainy Day",
        "album__id": 12,
        "count": 10,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Island Of Your Music",
        "album__id": 6,
        "count": 7,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Walking And Promises",
        "album__id": 10,
        "count": 7,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "Months Of Utopia",
        "album__id": 14,
        "count": 2,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "He Thinks He Did It",
        "album__id": 15,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "And Fireworks",
        "album__id": 17,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Things Of Dreams",
        "album__id": 16,
        "count": 1,
    },
]

top_albums_overall = deepcopy(top_albums)
for album in top_albums_overall:
    album["count"] *= 3

top_albums_2009 = deepcopy(top_albums)
for album in top_albums_2009:
    album["count"] *= 2

top_albums_2009_week_20 = [
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "album__title": "Lyrical And Things",
        "album__id": 7,
        "count": 51,
    },
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "He Can Sing",
        "album__id": 8,
        "count": 18,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "album__title": "Whispers Of Yesterday",
        "album__id": 9,
        "count": 15,
    },
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "So Do I",
        "album__id": 4,
        "count": 13,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "album__title": "A Way Of Never",
        "album__id": 5,
        "count": 6,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Dreaming Of Time",
        "album__id": 2,
        "count": 4,
    },
    {
        "artist__name": "Pathetic Genius",
        "album__title": "Memories Of My Thoughts",
        "album__id": 1,
        "count": 3,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "Months Of Utopia",
        "album__id": 14,
        "count": 2,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Island Of Your Music",
        "album__id": 6,
        "count": 2,
    },
    {
        "artist__name": "Oblivious Hosts",
        "album__title": "Summer Of My Enemy",
        "album__id": 3,
        "count": 2,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Dance For A Rainy Day",
        "album__id": 12,
        "count": 2,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "Call Of His Imagination",
        "album__id": 11,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "album__title": "He Thinks He Did It",
        "album__id": 15,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "And Fireworks",
        "album__id": 17,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Things Of Dreams",
        "album__id": 16,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Sweet Dreams Tonight",
        "album__id": 13,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "album__title": "Walking And Promises",
        "album__id": 10,
        "count": 1,
    },
]

top_albums_2009_05_11 = [
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "He Can Sing",
        "album__id": 8,
        "count": 8,
    },
    {
        "artist__name": "King Of All Memoirs",
        "album__title": "So Do I",
        "album__id": 4,
        "count": 7,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "album__title": "Whispers Of Yesterday",
        "album__id": 9,
        "count": 3,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Island Of Your Music",
        "album__id": 6,
        "count": 2,
    },
    {
        "artist__name": "Oblivious Hosts",
        "album__title": "Summer Of My Enemy",
        "album__id": 3,
        "count": 2,
    },
    {
        "artist__name": "Pathetic Genius",
        "album__title": "Memories Of My Thoughts",
        "album__id": 1,
        "count": 2,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "album__title": "A Way Of Never",
        "album__id": 5,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "And Fireworks",
        "album__id": 17,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "album__title": "Things Of Dreams",
        "album__id": 16,
        "count": 1,
    },
]

top_tracks = [
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Wake Up Call",
        "track__id": 10,
        "count": 38,
    },
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Long In The Tooth",
        "track__id": 8,
        "count": 18,
    },
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Mountain Out of a Molehill",
        "track__id": 4,
        "count": 17,
    },
    {
        "artist__name": "Buckets For You",
        "track__title": "Back To the Drawing Board",
        "track__id": 13,
        "count": 15,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Talk the Talk",
        "track__id": 29,
        "count": 14,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Beating Around the Bush",
        "track__id": 21,
        "count": 14,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "track__title": "Down To Earth",
        "track__id": 5,
        "count": 13,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Let Her Rip",
        "track__id": 15,
        "count": 11,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Hit Below The Belt",
        "track__id": 19,
        "count": 11,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Go For Broke",
        "track__id": 17,
        "count": 10,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Greased Lightning",
        "track__id": 1,
        "count": 7,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "On Cloud Nine",
        "track__id": 34,
        "count": 6,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Ring Any Bells?",
        "track__id": 24,
        "count": 6,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Lickety Split",
        "track__id": 2,
        "count": 6,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Fight Fire With Fire",
        "track__id": 3,
        "count": 5,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cut To The Chase",
        "track__id": 6,
        "count": 4,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Jack of All Trades Master of None",
        "track__id": 14,
        "count": 4,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Knuckle Down",
        "track__id": 25,
        "count": 3,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Right Off the Bat",
        "track__id": 12,
        "count": 2,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "My Cup of Tea",
        "track__id": 43,
        "count": 2,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "On the Ropes",
        "track__id": 33,
        "count": 2,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Top Drawer",
        "track__id": 18,
        "count": 2,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Elvis Has Left The Building",
        "track__id": 79,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "In a Pickle",
        "track__id": 51,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Like Father Like Son",
        "track__id": 20,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "A Piece of Cake",
        "track__id": 65,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "All Greek To Me",
        "track__id": 49,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "An Arm and a Leg",
        "track__id": 47,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Barking Up The Wrong Tree",
        "track__id": 39,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Beating a Dead Horse",
        "track__id": 57,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Burst Your Bubble",
        "track__id": 22,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Cut The Mustard",
        "track__id": 85,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Down To The Wire",
        "track__id": 7,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Drawing a Blank",
        "track__id": 76,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Easy As Pie",
        "track__id": 27,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Everything But The Kitchen Sink",
        "track__id": 41,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fish Out Of Water",
        "track__id": 56,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fit as a Fiddle",
        "track__id": 23,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Flea Market",
        "track__id": 45,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fool's Gold",
        "track__id": 35,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Go Out On a Limb",
        "track__id": 60,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Hands Down",
        "track__id": 26,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Head Over Heels",
        "track__id": 62,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Heads Up",
        "track__id": 42,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Hear, Hear",
        "track__id": 36,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "I Smell a Rat",
        "track__id": 69,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "If You Can't Stand the Heat, Get Out of the Kitchen",
        "track__id": 46,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "In the Red",
        "track__id": 53,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "It's Not All It's Cracked Up To Be",
        "track__id": 74,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Jaws of Life",
        "track__id": 70,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Jumping the Gun",
        "track__id": 31,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Keep Your Eyes Peeled",
        "track__id": 75,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Keep Your Shirt On",
        "track__id": 28,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Love Birds",
        "track__id": 50,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Lovey Dovey",
        "track__id": 55,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Money Doesn't Grow On Trees",
        "track__id": 32,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Needle In a Haystack",
        "track__id": 61,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "No-Brainer",
        "track__id": 44,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Not the Sharpest Tool in the Shed",
        "track__id": 58,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Off One's Base",
        "track__id": 38,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Playing For Keeps",
        "track__id": 9,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Poke Fun At",
        "track__id": 64,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Quick On the Draw",
        "track__id": 72,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Quick and Dirty",
        "track__id": 73,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Rain on Your Parade",
        "track__id": 54,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Raining Cats and Dogs",
        "track__id": 52,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Scot-free",
        "track__id": 68,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Short End of the Stick",
        "track__id": 40,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Swinging For the Fences",
        "track__id": 16,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "The Plot Thickens",
        "track__id": 83,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Tough It Out",
        "track__id": 71,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Tug of War",
        "track__id": 63,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Ugly Duckling",
        "track__id": 37,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Under the Weather",
        "track__id": 82,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "When the Rubber Hits the Road",
        "track__id": 78,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Wild Goose Chase",
        "track__id": 48,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Between a Rock and a Hard Place",
        "track__id": 30,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cry Over Spilt Milk",
        "track__id": 67,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Curiosity Killed The Cat",
        "track__id": 77,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Drive Me Nuts",
        "track__id": 81,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Jig Is Up",
        "track__id": 59,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Playing Possum",
        "track__id": 84,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Under Your Nose",
        "track__id": 66,
        "count": 1,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Throw In the Towel",
        "track__id": 11,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Par For the Course",
        "track__id": 80,
        "count": 1,
    },
]

top_tracks_overall = deepcopy(top_tracks)
for track in top_tracks_overall:
    track["count"] *= 3

top_tracks_2009 = deepcopy(top_tracks)
for track in top_tracks_2009:
    track["count"] *= 2

top_tracks_2009_week_20 = [
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Long In The Tooth",
        "track__id": 8,
        "count": 17,
    },
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Mountain Out of a Molehill",
        "track__id": 4,
        "count": 14,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Talk the Talk",
        "track__id": 29,
        "count": 8,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Wake Up Call",
        "track__id": 10,
        "count": 7,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "track__title": "Down To Earth",
        "track__id": 5,
        "count": 6,
    },
    {
        "artist__name": "Buckets For You",
        "track__title": "Back To the Drawing Board",
        "track__id": 13,
        "count": 3,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Greased Lightning",
        "track__id": 1,
        "count": 2,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Go For Broke",
        "track__id": 17,
        "count": 2,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Elvis Has Left The Building",
        "track__id": 79,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "In a Pickle",
        "track__id": 51,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Let Her Rip",
        "track__id": 15,
        "count": 1,
    },
    {
        "artist__name": "Consequently Loud",
        "track__title": "Like Father Like Son",
        "track__id": 20,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "A Piece of Cake",
        "track__id": 65,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "All Greek To Me",
        "track__id": 49,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "An Arm and a Leg",
        "track__id": 47,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Barking Up The Wrong Tree",
        "track__id": 39,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Beating a Dead Horse",
        "track__id": 57,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Burst Your Bubble",
        "track__id": 22,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Cut The Mustard",
        "track__id": 85,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Down To The Wire",
        "track__id": 7,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Drawing a Blank",
        "track__id": 76,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Easy As Pie",
        "track__id": 27,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Everything But The Kitchen Sink",
        "track__id": 41,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fish Out Of Water",
        "track__id": 56,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fit as a Fiddle",
        "track__id": 23,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Flea Market",
        "track__id": 45,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Fool's Gold",
        "track__id": 35,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Go Out On a Limb",
        "track__id": 60,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Hands Down",
        "track__id": 26,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Head Over Heels",
        "track__id": 62,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Heads Up",
        "track__id": 42,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Hear, Hear",
        "track__id": 36,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "I Smell a Rat",
        "track__id": 69,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "If You Can't Stand the Heat, Get Out of the Kitchen",
        "track__id": 46,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "In the Red",
        "track__id": 53,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "It's Not All It's Cracked Up To Be",
        "track__id": 74,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Jaws of Life",
        "track__id": 70,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Jumping the Gun",
        "track__id": 31,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Keep Your Eyes Peeled",
        "track__id": 75,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Keep Your Shirt On",
        "track__id": 28,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Love Birds",
        "track__id": 50,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Lovey Dovey",
        "track__id": 55,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Money Doesn't Grow On Trees",
        "track__id": 32,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Needle In a Haystack",
        "track__id": 61,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "No-Brainer",
        "track__id": 44,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Not the Sharpest Tool in the Shed",
        "track__id": 58,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Off One's Base",
        "track__id": 38,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Playing For Keeps",
        "track__id": 9,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Poke Fun At",
        "track__id": 64,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Quick On the Draw",
        "track__id": 72,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Quick and Dirty",
        "track__id": 73,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Rain on Your Parade",
        "track__id": 54,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Raining Cats and Dogs",
        "track__id": 52,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Scot-free",
        "track__id": 68,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Short End of the Stick",
        "track__id": 40,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Swinging For the Fences",
        "track__id": 16,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "The Plot Thickens",
        "track__id": 83,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Tough It Out",
        "track__id": 71,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Tug of War",
        "track__id": 63,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Ugly Duckling",
        "track__id": 37,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Under the Weather",
        "track__id": 82,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "When the Rubber Hits the Road",
        "track__id": 78,
        "count": 1,
    },
    {
        "artist__name": "Lenient Fascinated Apparatus",
        "track__title": "Wild Goose Chase",
        "track__id": 48,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cry Over Spilt Milk",
        "track__id": 67,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cut To The Chase",
        "track__id": 6,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Drive Me Nuts",
        "track__id": 81,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Jig Is Up",
        "track__id": 59,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Knuckle Down",
        "track__id": 25,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Playing Possum",
        "track__id": 84,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Under Your Nose",
        "track__id": 66,
        "count": 1,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Fight Fire With Fire",
        "track__id": 3,
        "count": 1,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Right Off the Bat",
        "track__id": 12,
        "count": 1,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Ring Any Bells?",
        "track__id": 24,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Beating Around the Bush",
        "track__id": 21,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Hit Below The Belt",
        "track__id": 19,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Jack of All Trades Master of None",
        "track__id": 14,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Lickety Split",
        "track__id": 2,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "My Cup of Tea",
        "track__id": 43,
        "count": 1,
    },
    {
        "artist__name": "Stop Nobodies",
        "track__title": "Top Drawer",
        "track__id": 18,
        "count": 1,
    },
]

top_tracks_2009_05_11 = [
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Mountain Out of a Molehill",
        "track__id": 4,
        "count": 8,
    },
    {
        "artist__name": "King Of All Memoirs",
        "track__title": "Long In The Tooth",
        "track__id": 8,
        "count": 7,
    },
    {
        "artist__name": "Buckets For You",
        "track__title": "Back To the Drawing Board",
        "track__id": 13,
        "count": 3,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Wake Up Call",
        "track__id": 10,
        "count": 2,
    },
    {
        "artist__name": "Bedeviling Instrument",
        "track__title": "Down To Earth",
        "track__id": 5,
        "count": 1,
    },
    {
        "artist__name": "Dancing Unquestioningly",
        "track__title": "Talk the Talk",
        "track__id": 29,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cry Over Spilt Milk",
        "track__id": 67,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Cut To The Chase",
        "track__id": 6,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Drive Me Nuts",
        "track__id": 81,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Jig Is Up",
        "track__id": 59,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Knuckle Down",
        "track__id": 25,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Playing Possum",
        "track__id": 84,
        "count": 1,
    },
    {
        "artist__name": "Lesser Paraphrase Variable",
        "track__title": "Under Your Nose",
        "track__id": 66,
        "count": 1,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Fight Fire With Fire",
        "track__id": 3,
        "count": 1,
    },
    {
        "artist__name": "Oblivious Hosts",
        "track__title": "Right Off the Bat",
        "track__id": 12,
        "count": 1,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Greased Lightning",
        "track__id": 1,
        "count": 1,
    },
    {
        "artist__name": "Pathetic Genius",
        "track__title": "Ring Any Bells?",
        "track__id": 24,
        "count": 1,
    },
]

counts_yearly = [
    {"year": datetime.date(2007, 1, 1), "count": 136},
    {"year": datetime.date(2008, 1, 1), "count": 137},
    {"year": datetime.date(2009, 1, 1), "count": 546},
]

counts_monthly_2009 = [
    {"month": datetime.date(2009, 1, 1), "count": 23},
    {"month": datetime.date(2009, 2, 1), "count": 20},
    {"month": datetime.date(2009, 3, 1), "count": 32},
    {"month": datetime.date(2009, 4, 1), "count": 21},
    {"month": datetime.date(2009, 5, 1), "count": 273},
    {"month": datetime.date(2009, 6, 1), "count": 28},
    {"month": datetime.date(2009, 7, 1), "count": 33},
    {"month": datetime.date(2009, 8, 1), "count": 32},
    {"month": datetime.date(2009, 9, 1), "count": 19},
    {"month": datetime.date(2009, 10, 1), "count": 19},
    {"month": datetime.date(2009, 11, 1), "count": 21},
    {"month": datetime.date(2009, 12, 1), "count": 25},
]

counts_weekly_2009_05 = [
    {"week": datetime.date(2009, 4, 27), "count": 41},
    {"week": datetime.date(2009, 5, 4), "count": 61},
    {"week": datetime.date(2009, 5, 11), "count": 130},
    {"week": datetime.date(2009, 5, 18), "count": 7},
    {"week": datetime.date(2009, 5, 25), "count": 34},
]

counts_daily_2009_05_11_to_2009_05_17 = [
    {"day": datetime.date(2009, 5, 11), "count": 33},
    {"day": datetime.date(2009, 5, 12), "count": 62},
    {"day": datetime.date(2009, 5, 13), "count": 8},
    {"day": datetime.date(2009, 5, 14), "count": 4},
    {"day": datetime.date(2009, 5, 15), "count": 6},
    {"day": datetime.date(2009, 5, 17), "count": 17},
]

toplistdata_artists_2007 = TopListData(
    category="artists",
    toplist=top_artists_2007,
    total_listens=136,
    max_listen_count=29,
    type="whatever",
)

toplistdata_artists_2008 = TopListData(
    category="artists",
    toplist=top_artists_2008,
    total_listens=137,
    max_listen_count=31,
    type="whatever",
)

toplistdata_artists_2007_and_2008 = TopListData(
    category="artists",
    toplist=top_artists,
    total_listens=273,
    max_listen_count=52,
    type="whatever",
)
