# Generated by Django 5.0.6 on 2024-09-27 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0013_rename_bot_key_bottrade_bot_plan_bottrade_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottrade',
            name='bot_plan',
        ),
    ]
