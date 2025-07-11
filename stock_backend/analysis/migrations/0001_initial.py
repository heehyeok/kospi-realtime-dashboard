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
            name='ClusteringCriterion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClusteringResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.IntegerField()),
                ('criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.clusteringcriterion')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusterings', to='stocks.stock')),
            ],
            options={
                'unique_together': {('stock', 'criterion')},
            },
        ),
    ]
