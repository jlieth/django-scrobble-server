from django.contrib import admin

from scrobble_server.api.v12.models import Client, ScrobbleSession, MD5AuthHash


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["client_id", "client_version", "banned", "created", "last_seen"]
    list_filter = ["created", "last_seen"]
    search_fields = ["client_id"]
    readonly_fields = ["created", "last_seen"]


@admin.register(ScrobbleSession)
class CustomSessionAdmin(admin.ModelAdmin):
    list_display = ["__str__", "profile", "client", "created"]
    readonly_fields = ["created", "profile", "client"]
    date_hierarchy = "created"


@admin.register(MD5AuthHash)
class MD5AuthHashAdmin(admin.ModelAdmin):
    list_display = ["profile", "hash"]
    readonly_fields = ["profile"]
