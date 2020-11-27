# Generated by Django 3.1.3 on 2020-11-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
                ('email', models.CharField(max_length=320, verbose_name='email')),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]