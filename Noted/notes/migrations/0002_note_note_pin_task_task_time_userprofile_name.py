# Generated by Django 4.1 on 2023-04-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_pin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='task_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Username', max_length=20),
        ),
    ]
