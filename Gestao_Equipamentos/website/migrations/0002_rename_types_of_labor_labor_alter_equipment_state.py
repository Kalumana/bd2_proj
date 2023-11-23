# Generated by Django 4.2.4 on 2023-11-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Types_of_Labor',
            new_name='Labor',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='state',
            field=models.CharField(choices=[('analysing', 'Em analise'), ('producing', 'A produzir'), ('produced', 'Produzido'), ('delivery', 'Entregue')], default='ANALYSING', max_length=9),
        ),
    ]
