# Generated by Django 4.0.6 on 2022-08-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('read', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MyPayroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('read', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MyStudioSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('read', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=40)),
                ('stage_name', models.CharField(max_length=40)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user-profile')),
                ('code_number', models.IntegerField()),
            ],
        ),
    ]
