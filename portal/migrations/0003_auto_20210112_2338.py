# Generated by Django 3.1.4 on 2021-01-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_job_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='permission',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]