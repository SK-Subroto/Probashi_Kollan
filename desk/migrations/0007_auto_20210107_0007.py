# Generated by Django 3.1.4 on 2021-01-06 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210107_0007'),
        ('desk', '0006_auto_20201223_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.attendant'),
        ),
    ]
