# Generated by Django 4.2.10 on 2024-03-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0002_restaurantes_horario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantes',
            old_name='endereco',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='restaurantes',
            old_name='especialidade',
            new_name='cuisine',
        ),
        migrations.RenameField(
            model_name='restaurantes',
            old_name='horario',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='restaurantes',
            old_name='telefone',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='restaurantes',
            old_name='nome',
            new_name='working_hours',
        ),
        migrations.AlterField(
            model_name='restaurantes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
