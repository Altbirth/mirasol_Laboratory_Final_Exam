# Generated by Django 4.2.7 on 2023-12-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_remove_toptierwaifu_anime_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestanimeofalltime',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
