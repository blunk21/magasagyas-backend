# Generated by Django 4.2.4 on 2023-10-21 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0002_rename_creation_date_config_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='config',
            options={'managed': False},
        ),
    ]