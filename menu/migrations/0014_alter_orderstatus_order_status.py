# Generated by Django 4.2.6 on 2024-05-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='order_status',
            field=models.CharField(default='Received', max_length=255),
        ),
    ]
