# Generated by Django 3.0.8 on 2020-10-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_notification_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='fail_success',
            field=models.BooleanField(default=True),
        ),
    ]
