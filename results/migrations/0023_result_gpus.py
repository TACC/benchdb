# Generated by Django 3.1 on 2021-01-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0022_auto_20210121_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='gpus',
            field=models.IntegerField(default=0),
        ),
    ]
