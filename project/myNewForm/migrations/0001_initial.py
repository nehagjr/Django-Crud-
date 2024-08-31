# Generated by Django 5.1 on 2024-08-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_city', models.CharField(max_length=50)),
                ('stu_mobile', models.IntegerField()),
                ('stu_password', models.CharField(max_length=25)),
            ],
        ),
    ]
