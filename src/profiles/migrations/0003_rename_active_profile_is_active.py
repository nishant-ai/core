# Generated by Django 3.2.5 on 2021-08-02 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='active',
            new_name='is_active',
        ),
    ]
