# Generated by Django 4.2 on 2023-07-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contatocliente_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatocliente',
            name='cidade',
            field=models.CharField(choices=[('Selecione', '--------'), ('João Pessoa', 'João Pessoa'), ('Campina Grande', 'Campina Grande')], default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='contatocliente',
            name='tipo',
            field=models.CharField(choices=[('Selecione', '--------'), ('Preciso de um Cuidador', 'Preciso de um cuidador'), ('Sou um Cuidador', 'Sou um cuidador')], default='', max_length=25),
        ),
    ]
