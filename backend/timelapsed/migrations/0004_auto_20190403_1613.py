# Generated by Django 2.1.7 on 2019-04-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timelapsed', '0003_auto_20190326_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date_range',
            old_name='Date',
            new_name='Begin_Date',
        ),
        migrations.AddField(
            model_name='date_range',
            name='End_Date',
            field=models.DateField(null=True),
        ),
    ]