# Generated by Django 4.1 on 2023-09-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_tituloblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='tituloblog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
