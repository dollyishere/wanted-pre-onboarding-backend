# Generated by Django 5.0.8 on 2024-08-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment_app', '0003_rename_company_recruitment_company_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitment',
            name='compensation',
            field=models.IntegerField(default=0),
        ),
    ]
