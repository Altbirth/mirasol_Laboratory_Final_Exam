# Generated by Django 4.2.7 on 2023-12-29 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_animeaward_getdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animelist',
            old_name='duration_minutes',
            new_name='episode',
        ),
    ]
