# Generated by Django 4.2.7 on 2023-11-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=180)),
                ('descricao', models.TextField()),
                ('tecnologia', models.CharField(max_length=20)),
                ('imagem', models.FilePathField(path='/img')),
            ],
        ),
    ]