# Generated by Django 5.0.2 on 2024-02-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_applicant',
            field=models.BooleanField(default=False),
        ),
    ]
