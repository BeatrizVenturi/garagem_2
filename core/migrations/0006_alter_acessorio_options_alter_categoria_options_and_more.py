# Generated by Django 5.0.6 on 2024-08-01 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_marca"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="acessorio",
            options={"verbose_name": "Acessório", "verbose_name_plural": "Acessórios"},
        ),
        migrations.AlterModelOptions(
            name="categoria",
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
        migrations.AlterModelOptions(
            name="marca",
            options={"verbose_name": "Marca", "verbose_name_plural": "Marcas"},
        ),
    ]
