# Generated by Django 3.0.7 on 2020-07-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_result_nodelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
