# Generated by Django 4.1.6 on 2023-02-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_hallbook_internet_alter_hallbook_lamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallbook',
            name='Internet',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hallbook',
            name='Lamp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hallbook',
            name='Mic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hallbook',
            name='projector',
            field=models.BooleanField(default=False),
        ),
    ]
