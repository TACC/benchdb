# Generated by Django 3.2.12 on 2022-03-18 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0028_auto_20210714_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='elapsed_time',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='submit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
