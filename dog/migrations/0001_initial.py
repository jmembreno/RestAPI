# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-24 02:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('T', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=6)),
                ('Friendliness', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Trainability', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Sheddingamount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Exerciseneed', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('favoritefood', models.CharField(max_length=50)),
                ('favoritetoy', models.CharField(max_length=50)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='dog.Breed')),
            ],
        ),
    ]
