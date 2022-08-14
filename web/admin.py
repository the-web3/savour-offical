from django.contrib import admin

from web.models import (
    SavorTeam,
    Position,
    WantJoin,
)

@admin.register(SavorTeam)
class SavorTeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "name")


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "name")


@admin.register(WantJoin)
class WantJoinAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "is_active")
    list_per_page = 50
    ordering = ("-created_at",)
    list_display_links = ("id", "phone")

