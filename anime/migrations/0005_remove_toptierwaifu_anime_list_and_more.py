# Generated by Django 4.2.7 on 2023-12-29 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_animationstudio_foundeddate_toptierwaifu_resultdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toptierwaifu',
            name='anime_list',
        ),
        migrations.AddField(
            model_name='toptierwaifu',
            name='anime_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anime.animelist'),
        ),
    ]
