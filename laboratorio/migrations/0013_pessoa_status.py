# Generated by Django 4.0.6 on 2022-09-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0012_alter_pessoa_numero_cracha'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='status',
            field=models.CharField(choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')], default='Ativo', max_length=25, verbose_name='Status'),
        ),
    ]