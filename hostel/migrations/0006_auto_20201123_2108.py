# Generated by Django 3.0.3 on 2020-11-24 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_auto_20201123_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('One in One', 'One in One'), ('Two in One', 'Two in One'), ('Three in One', 'Three in One'), ('4 in 1', 'Four in One')], max_length=12),
        ),
    ]
