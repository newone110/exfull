# Generated by Django 5.0.6 on 2024-09-30 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dash', '0017_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='User',
        ),
    ]
