# Generated by Django 3.1.7 on 2021-02-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210107_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='photo',
            field=models.ImageField(blank=True, default='default_profile_2.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='immigrant',
            name='photo',
            field=models.ImageField(blank=True, default='default_profile.jpg', null=True, upload_to=''),
        ),
    ]
