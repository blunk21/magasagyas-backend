# Generated by Django 4.2.4 on 2023-10-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField()),
                ('server_timestamp', models.TimeField(auto_now_add=True)),
                ('timestamp', models.TimeField()),
            ],
            options={
                'db_table': 'messages',
            },
        ),
    ]
