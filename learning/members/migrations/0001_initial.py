# Generated by Django 4.2.5 on 2023-09-16 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=25)),
                ('l_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
