# Generated by Django 3.0.8 on 2020-07-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='friday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='monday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='saturday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='sunday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thursday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tuesday',
            field=models.CharField(default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wednesday',
            field=models.CharField(default='---', max_length=100),
        ),
    ]
