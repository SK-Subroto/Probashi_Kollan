# Generated by Django 3.1.7 on 2021-02-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0012_remove_notice_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='region',
            field=models.CharField(choices=[('australia', 'Australia'), ('canada', 'Canada'), ('france', 'France'), ('germany', 'Germany'), ('malaysia', 'Malaysia')], max_length=20, null=True),
        ),
    ]
