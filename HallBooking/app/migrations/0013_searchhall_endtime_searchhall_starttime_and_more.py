# Generated by Django 4.1.6 on 2023-03-08 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_hallbook_equipments'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhall',
            name='EndTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='searchhall',
            name='StartTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='searchhall',
            name='Hallname',
            field=models.CharField(max_length=30),
        ),
    ]
