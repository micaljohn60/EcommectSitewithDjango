# Generated by Django 3.1.2 on 2020-10-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_item_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
