# Generated by Django 3.0.8 on 2020-10-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_notification_fail_success'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='fail_success',
            new_name='success_fail',
        ),
    ]
