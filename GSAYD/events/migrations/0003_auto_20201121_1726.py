# Generated by Django 3.1 on 2020-11-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='title',
            new_name='event_name',
        ),
    ]