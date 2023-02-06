# Generated by Django 4.1.5 on 2023-02-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_ad_category_location_user_delete_ads_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.AddField(
            model_name='user',
            name='location_id',
            field=models.ManyToManyField(to='ads.location'),
        ),
    ]
