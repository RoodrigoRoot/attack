# Generated by Django 3.0.7 on 2020-06-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_link', models.CharField(max_length=50, verbose_name='Nombre del Link')),
                ('link', models.URLField(verbose_name='Enlace')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Enlace',
                'verbose_name_plural': 'Enlaces',
            },
        ),
    ]
