# Generated by Django 3.1.4 on 2020-12-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0005_auto_20201223_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_date',
            field=models.DateTimeField(null=True),
        ),
    ]
