# Generated by Django 4.2.10 on 2024-03-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_cuisine_alter_restaurantes_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantes',
            name='cuisine',
            field=models.CharField(max_length=100),
        ),
    ]
