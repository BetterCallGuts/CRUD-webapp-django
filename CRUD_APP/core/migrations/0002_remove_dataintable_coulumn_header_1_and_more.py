# Generated by Django 4.2 on 2023-06-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataintable',
            name='coulumn_header_1',
        ),
        migrations.RemoveField(
            model_name='dataintable',
            name='coulumn_header_2',
        ),
        migrations.RemoveField(
            model_name='dataintable',
            name='coulumn_header_3',
        ),
        migrations.RemoveField(
            model_name='dataintable',
            name='coulumn_header_4',
        ),
        migrations.AddField(
            model_name='table',
            name='coulumn_header_1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='table',
            name='coulumn_header_2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='table',
            name='coulumn_header_3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='table',
            name='coulumn_header_4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dataintable',
            name='coulumn1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dataintable',
            name='coulumn2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dataintable',
            name='coulumn3',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='dataintable',
            name='coulumn4',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
