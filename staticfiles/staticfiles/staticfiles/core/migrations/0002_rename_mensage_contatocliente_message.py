# Generated by Django 4.2 on 2023-04-24 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contatocliente',
            old_name='mensage',
            new_name='message',
        ),
    ]
