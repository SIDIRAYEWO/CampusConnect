from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organization",
        "organizer",
        "event_type",
        "status",
        "start_time",
        "created_at",
    )

    list_filter = (
        "organization",
        "event_type",
        "status",
    )

    search_fields = (
        "title",
        "description",
        "organization__name",
        "organizer__username",
        "venue",
    )

    ordering = (
        "start_time",
    )