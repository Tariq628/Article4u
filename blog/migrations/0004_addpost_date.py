# Generated by Django 3.2 on 2021-09-21 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_addpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
