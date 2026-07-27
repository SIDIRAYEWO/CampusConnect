from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "programme",
        "faculty",
        "year_of_study",
    )

    search_fields = (
        "student_id",
        "user__username",
        "programme",
        "faculty",
    )

    list_filter = (
        "faculty",
        "year_of_study",
    )