# Generated by Django 3.1 on 2021-07-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0027_application_script'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='stderr',
            field=models.CharField(default='stdout', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='stdout',
            field=models.CharField(default='stderr', max_length=50),
            preserve_default=False,
        ),
    ]
