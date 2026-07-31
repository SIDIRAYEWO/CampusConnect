from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "organization",
        "author",
        "priority",
        "status",
        "published_at",
        "created_at",
    ]

    list_filter = [
        "organization",
        "priority",
        "status",
    ]

    search_fields = [
        "title",
        "content",
        "organization__name",
        "author__username",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
        "deleted_at",
    ]