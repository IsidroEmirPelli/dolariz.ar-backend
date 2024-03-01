# Generated by Django 4.0.7 on 2024-03-01 04:11

import core.enums
import core.models
from django.db import migrations, models
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('uuid', models.CharField(default=core.models.generate_dolar_uuid, help_text='Unique UUID for the dolar', max_length=16, primary_key=True, serialize=False)),
                ('price_buy', models.DecimalField(decimal_places=2, help_text='Price to buy the dolar', max_digits=10)),
                ('price_sell', models.DecimalField(decimal_places=2, help_text='Price to sell the dolar', max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Date and time of the dolar')),
                ('type_of_quote', django_enumfield.db.fields.EnumField(enum=core.enums.DolarType, help_text='Type of quote', max_length=10)),
                ('extra_data', models.JSONField(help_text='Extra data for the dolar')),
            ],
        ),
    ]
