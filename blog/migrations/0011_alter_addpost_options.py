# Generated by Django 3.2 on 2021-10-06 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_addpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addpost',
            options={'get_latest_by': 'order_date'},
        ),
    ]
