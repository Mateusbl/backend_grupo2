# Generated by Django 4.2.10 on 2024-03-02 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0005_alter_restaurantes_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='restaurantes', to='restaurantes.cuisine'),
        ),
    ]
