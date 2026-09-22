from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = (
        'student_name',
        'item_name',
        'report_type',
        'category',
        'location',
        'status',
        'date_time',
    )

    list_filter = (
        'report_type',
        'category',
        'status',
    )

    search_fields = (
        'student_name',
        'enrollment_number',
        'item_name',
        'location',
    )