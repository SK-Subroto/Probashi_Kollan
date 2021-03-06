# Generated by Django 3.1.4 on 2020-12-21 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Immigrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immigrant_id', models.CharField(max_length=20, null=True)),
                ('immigrant_name', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('dob', models.DateField(null=True)),
                ('job_status', models.BooleanField(default=False, null=True)),
                ('job_desig', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('county', models.CharField(max_length=50, null=True)),
                ('contact_nb', models.CharField(max_length=20, null=True)),
                ('passport_nb', models.CharField(max_length=20, null=True)),
                ('visa_nb', models.CharField(max_length=20, null=True)),
                ('stay_duration', models.FloatField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendant_id', models.CharField(max_length=20, null=True)),
                ('attendant_name', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('dob', models.DateField(null=True)),
                ('contact_nb', models.CharField(max_length=20, null=True)),
                ('passport_nb', models.CharField(max_length=20, null=True)),
                ('category', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
