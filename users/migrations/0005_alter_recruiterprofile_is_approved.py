# Generated by Django 5.2.4 on 2025-07-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_recruiterprofile_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiterprofile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
