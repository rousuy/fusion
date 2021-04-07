# Generated by Django 3.2 on 2021-04-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=120, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', 'foguete'), ('lni-laptop-phone', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Camadas'), ('lni-leaf', 'Folhas'), ('lni-leaf', 'Folhas')], max_length=16, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]
