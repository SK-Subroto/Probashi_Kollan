# Generated by Django 3.1.7 on 2021-02-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20210120_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='region',
            field=models.CharField(choices=[('australia', 'Australia'), ('canada', 'Canada'), ('france', 'France'), ('germany', 'Germany'), ('malaysia', 'Malaysia')], max_length=20, null=True),
        ),
    ]
