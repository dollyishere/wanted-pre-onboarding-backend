# Generated by Django 5.0.8 on 2024-08-12 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment_app', '0002_alter_recruitment_company_alter_resume_recruitment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruitment',
            old_name='company',
            new_name='company_id',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='recruitment',
            new_name='recruitment_id',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='user',
            new_name='user_id',
        ),
    ]
