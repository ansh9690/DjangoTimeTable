# Generated by Django 3.0.8 on 2020-07-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200730_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='friday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='monday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='saturday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='sunday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thursday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tuesday',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wednesday',
            field=models.CharField(max_length=100),
        ),
    ]
