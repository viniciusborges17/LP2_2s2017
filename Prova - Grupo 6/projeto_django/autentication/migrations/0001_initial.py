# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('ra', models.IntegerField(unique=True, verbose_name='RA')),
                ('password', models.CharField(max_length=200, verbose_name='Senha')),
                ('nome', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('perfil', models.CharField(max_length=1, verbose_name='Perfil')),
            ],
            options={
                'db_table': 'USUARIO',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
