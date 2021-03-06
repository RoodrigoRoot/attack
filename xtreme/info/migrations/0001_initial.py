# Generated by Django 3.0.7 on 2020-06-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='tech', verbose_name='Image')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Tecnología',
                'verbose_name_plural': 'Tecnologías',
            },
        ),
    ]
