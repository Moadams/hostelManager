# Generated by Django 3.0.3 on 2020-11-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_auto_20201123_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='spaces_available',
            field=models.PositiveIntegerField(default=0),
        ),
    ]