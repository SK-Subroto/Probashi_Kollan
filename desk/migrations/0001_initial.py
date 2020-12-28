# Generated by Django 3.1.4 on 2020-12-21 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('notice_date', models.DateField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('meeting_date', models.DateField(null=True)),
                ('attendant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.attendant')),
                ('immigrant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.immigrant')),
            ],
        ),
    ]
