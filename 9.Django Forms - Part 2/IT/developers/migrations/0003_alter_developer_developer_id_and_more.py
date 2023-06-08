# Generated by Django 4.2 on 2023-06-08 11:38

import IT.developers.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0002_alter_developer_developer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='developer_id',
            field=models.PositiveIntegerField(error_messages={'unique': 'ID already registered!'}, unique=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30), IT.developers.validators.min_length_validator]),
        ),
        migrations.AlterField(
            model_name='developer',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), IT.developers.validators.max_length_validator]),
        ),
    ]
