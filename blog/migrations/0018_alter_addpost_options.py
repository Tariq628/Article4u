# Generated by Django 3.2.8 on 2021-10-17 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_addpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addpost',
            options={'get_latest_by': 'date'},
        ),
    ]
