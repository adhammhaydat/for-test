# Generated by Django 4.0 on 2021-12-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='status',
            field=models.CharField(blank=True, default='pending', max_length=32),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(blank=True, default='title', max_length=255),
        ),
    ]
