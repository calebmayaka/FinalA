# Generated by Django 5.1.7 on 2025-03-27 13:30

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_applicant', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='companyprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticationapp.custommodel')),
            ],
        ),
        migrations.CreateModel(
            name='applicantprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, max_length=255, null=True)),
                ('linkedin', models.TextField(blank=True, max_length=255, null=True)),
                ('twitter', models.TextField(blank=True, max_length=255, null=True)),
                ('facebook', models.TextField(blank=True, max_length=255, null=True)),
                ('reddit', models.TextField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='authenticationapp.custommodel')),
            ],
        ),
    ]
