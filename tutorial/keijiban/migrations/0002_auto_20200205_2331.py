# Generated by Django 2.2.7 on 2020-02-05 14:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keijiban', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Keijiban',
            new_name='Post',
        ),
    ]