from django.contrib import admin
from .models import TimeTable
from import_export.admin import ImportExportModelAdmin


@admin.register(TimeTable)
class TimeTableAdmin(ImportExportModelAdmin):
    list_display = ('id', 'time', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
