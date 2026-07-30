from django.contrib import admin

from .models import (
    Club,
    ClubMembership,
)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "advisor_name",
        "is_verified",
        "created_at",
    )

    list_filter = (
        "category",
        "is_verified",
    )

    search_fields = (
        "name",
        "description",
        "advisor_name",
    )

    ordering = (
        "name",
    )


@admin.register(ClubMembership)
class ClubMembershipAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "club",
        "role",
        "status",
        "joined_at",
    )

    list_filter = (
        "role",
        "status",
        "club",
    )

    search_fields = (
        "user__username",
        "club__name",
    )

    ordering = (
        "club",
        "user",
    )