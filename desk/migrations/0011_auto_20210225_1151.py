# Generated by Django 3.1.7 on 2021-02-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0010_auto_20210225_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='region',
            field=models.CharField(choices=[('australia', 'Australia'), ('canada', 'Canada'), ('france', 'France'), ('germany', 'Germany'), ('malaysia', 'Malaysia')], max_length=20, null=True),
        ),
    ]
