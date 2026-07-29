from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "organizer",
        "event_type",
        "audience",
        "status",
        "start_time",
        "created_at",
    )

    list_filter = (
        "event_type",
        "audience",
        "status",
    )

    search_fields = (
        "title",
        "description",
        "organizer__username",
        "venue",
    )

    ordering = (
        "start_time",
    )