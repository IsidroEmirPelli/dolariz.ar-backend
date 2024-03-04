# Generated by Django 4.2.10 on 2024-03-02 21:45

import core.models
from django.db import migrations, models
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dollar',
            fields=[
                ('uuid', models.CharField(default=core.models.generate_dollar_uuid, help_text='Unique UUID for the dollar', max_length=16, primary_key=True, serialize=False)),
                ('price_buy', models.DecimalField(decimal_places=2, help_text='Price to buy the dollar', max_digits=10)),
                ('price_sell', models.DecimalField(decimal_places=2, help_text='Price to sell the dollar', max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Date and time of the dollar')),
                ('type_of_quote', django_enumfield.db.fields.EnumField(enum=core.models.DollarType, help_text='Type of quote')),
                ('extra_data', models.JSONField(help_text='Extra data for the dollar')),
            ],
        ),
    ]
