from django.contrib import admin

from scrobble_server.core.models.cache import ChartsCache
from scrobble_server.core.models.music import Album, AlbumTrackUnit, Artist, Track
from scrobble_server.core.models.profile import Profile
from scrobble_server.core.models.submissions import NowPlaying, Scrobble


# Inlines
class InlineBase(admin.TabularInline):
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj=None):
        return False


class NowPlayingInline(InlineBase):
    model = NowPlaying
    fields = ["date", "artist_name", "track_title", "album_title"]
    readonly_fields = fields


class AlbumInline(InlineBase):
    model = Album


class TrackInline(InlineBase):
    model = Track


class AlbumTrackUnitInline(InlineBase):
    model = AlbumTrackUnit
    raw_id_fields = ["album", "track"]


# Profile-related models
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [NowPlayingInline]


@admin.register(Scrobble)
class ScrobbleAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "profile",
        "artist_name",
        "track_title",
        "album_title",
        "length",
        "tracknumber",
    ]
    list_filter = ["date"]
    date_hierarchy = "date"
    search_fields = ["track_title", "artist_name", "album_title"]
    raw_id_fields = ["profile", "artist", "album", "track"]
    readonly_fields = ["date"]


@admin.register(NowPlaying)
class NowPlayingAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "profile",
        "artist_name",
        "track_title",
        "album_title",
        "length",
        "tracknumber",
        "is_over",
    ]
    list_filter = ["date"]
    raw_id_fields = ["profile", "artist", "album", "track"]
    readonly_fields = ["date"]


# Music-related models
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    inlines = [AlbumInline, TrackInline]


@admin.register(Album, Track)
class AlbumAndTrackAdmin(admin.ModelAdmin):
    list_display = ["title", "artist"]
    search_fields = ["title", "artist__name"]
    raw_id_fields = ["artist"]
    inlines = [AlbumTrackUnitInline]


@admin.register(AlbumTrackUnit)
class AlbumTrackUnitAdmin(admin.ModelAdmin):
    list_display = ["track", "album", "tracknumber", "length"]
    search_fields = ["album__title, track__title"]
    raw_id_fields = ["album", "track"]


# Chart Cache
@admin.register(ChartsCache)
class UserChartCacheAdmin(admin.ModelAdmin):
    list_display = [
        "content_type",
        "obj",
        "category",
        "timespan",
        "date",
        "total_listens",
        "max_listen_count",
    ]
    list_filter = ["category", "timespan", "date"]
