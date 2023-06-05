# Generated by Django 4.2.1 on 2023-06-05 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacao',
            name='endereco',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 5, 4, 18, 32, 755357, tzinfo=datetime.timezone.utc), verbose_name='Date modified'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 5, 4, 18, 32, 755357, tzinfo=datetime.timezone.utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='doacaoseries',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 5, 4, 18, 32, 753365, tzinfo=datetime.timezone.utc), verbose_name='Date published'),
        ),
    ]