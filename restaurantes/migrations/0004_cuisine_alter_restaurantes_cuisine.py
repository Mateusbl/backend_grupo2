# Generated by Django 4.2.10 on 2024-03-02 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0003_rename_endereco_restaurantes_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuisine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurantes',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cuisine_restaurantes', to='restaurantes.cuisine'),
        ),
    ]
