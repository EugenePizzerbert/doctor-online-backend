# Generated by Django 2.1.1 on 2018-11-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_doctorprofile_is_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='viewers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]