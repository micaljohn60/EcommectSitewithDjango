# Generated by Django 3.0.8 on 2020-09-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200925_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pending',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
