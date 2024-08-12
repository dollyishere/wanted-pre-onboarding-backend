# Generated by Django 5.0.8 on 2024-08-12 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recruitment_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=255)),
                ('compensation', models.IntegerField()),
                ('content', models.TextField()),
                ('skill', models.CharField(max_length=255)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recruitment_app.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='resume',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resume_id', models.AutoField(primary_key=True, serialize=False)),
                ('recruitment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recruitment_app.recruitment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recruitment_app.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
