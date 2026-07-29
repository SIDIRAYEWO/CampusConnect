from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "audience",
        "priority",
        "status",
        "published_at",
        "created_at",
    )

    list_filter = (
        "audience",
        "priority",
        "status",
        "created_at",
        "published_at",
    )

    search_fields = (
        "title",
        "content",
        "author__username",
        "author__email",
    )

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25