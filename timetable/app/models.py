from django.db import models
from django.forms import ModelForm


class TimeTable(models.Model):
    time = models.CharField(max_length=20)
    monday = models.CharField(max_length=100)
    tuesday = models.CharField(max_length=100)
    wednesday = models.CharField(max_length=100)
    thursday = models.CharField(max_length=100)
    friday = models.CharField(max_length=100)
    saturday = models.CharField(max_length=100)
    sunday = models.CharField(max_length=100)


class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = ['time', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', ]


class UpdateTimeTableForm(ModelForm):
    class Meta:
        model = TimeTable
        fields = ['time', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', ]
