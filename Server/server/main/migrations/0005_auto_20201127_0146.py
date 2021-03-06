# Generated by Django 3.1.3 on 2020-11-26 23:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_anime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'verbose_name': 'Anime', 'verbose_name_plural': 'Animes'},
        ),
        migrations.AddField(
            model_name='anime',
            name='genre',
            field=models.CharField(default={'genre': 'undefined', 'released': django.utils.timezone.now}, max_length=25, verbose_name='genre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='released',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='released'),
            preserve_default=False,
        ),
    ]
