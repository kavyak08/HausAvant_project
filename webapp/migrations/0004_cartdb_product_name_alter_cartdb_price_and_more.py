# Generated by Django 5.1.2 on 2024-11-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_cartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cartdb',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartdb',
            name='Total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
