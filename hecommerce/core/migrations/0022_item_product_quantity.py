# Generated by Django 3.1.2 on 2020-10-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201004_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
