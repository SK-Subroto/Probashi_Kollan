# Generated by Django 3.1.7 on 2021-02-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_auto_20210225_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='region',
            field=models.CharField(choices=[('australia', 'Australia'), ('canada', 'Canada'), ('france', 'France'), ('germany', 'Germany'), ('malaysia', 'Malaysia')], max_length=20, null=True),
        ),
    ]
