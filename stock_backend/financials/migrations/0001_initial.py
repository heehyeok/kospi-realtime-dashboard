# Generated by Django 5.1.7 on 2025-05-28 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('revenue', models.BigIntegerField()),
                ('operating_income', models.BigIntegerField()),
                ('net_income', models.BigIntegerField()),
                ('eps', models.FloatField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financials', to='stocks.stock')),
            ],
            options={
                'ordering': ['-year'],
                'unique_together': {('stock', 'year')},
            },
        ),
    ]
