# Generated by Django 4.1.10 on 2023-12-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_username_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='manager',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]