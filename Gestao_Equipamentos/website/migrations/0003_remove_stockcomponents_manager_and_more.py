# Generated by Django 4.2.4 on 2023-11-22 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_types_of_labor_labor_alter_equipment_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockcomponents',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='stockequipments',
            name='manager',
        ),
    ]