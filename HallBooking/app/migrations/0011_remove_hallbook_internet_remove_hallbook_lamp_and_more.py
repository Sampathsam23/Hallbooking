# Generated by Django 4.1.6 on 2023-03-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_searchhall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hallbook',
            name='Internet',
        ),
        migrations.RemoveField(
            model_name='hallbook',
            name='Lamp',
        ),
        migrations.RemoveField(
            model_name='hallbook',
            name='Mic',
        ),
        migrations.RemoveField(
            model_name='hallbook',
            name='projector',
        ),
        migrations.AddField(
            model_name='hallbook',
            name='Equipments',
            field=models.CharField(default='none', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hallbook',
            name='Department',
            field=models.CharField(max_length=50),
        ),
    ]
