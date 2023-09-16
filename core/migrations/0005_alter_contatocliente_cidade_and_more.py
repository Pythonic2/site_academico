# Generated by Django 4.1 on 2023-09-15 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_contatocliente_cidade_alter_contatocliente_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatocliente',
            name='cidade',
            field=models.CharField(choices=[('Nao Selecionado', '--------'), ('João Pessoa', 'João Pessoa'), ('Campina Grande', 'Campina Grande')], default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='contatocliente',
            name='tipo',
            field=models.CharField(choices=[('Nao Selecionado', '--------'), ('Preciso de um Cuidador', 'Preciso de um cuidador'), ('Sou um Cuidador', 'Sou um cuidador')], default='', max_length=25),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=200)),
                ('texto', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/')),
                ('video_url', models.URLField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
