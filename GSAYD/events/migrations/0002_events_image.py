# Generated by Django 3.1 on 2020-11-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(default='', upload_to='media/images/events'),
        ),
    ]