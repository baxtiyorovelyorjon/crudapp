# Generated by Django 4.0.4 on 2022-04-13 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ism')),
                ('groups', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='age',
            field=models.IntegerField(verbose_name='yoshi:'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email:'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Ism:'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Familiya:'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.IntegerField(verbose_name='Tel:'),
        ),
        migrations.CreateModel(
            name='AlbumModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.musicmodel', verbose_name='Ism')),
            ],
        ),
    ]
