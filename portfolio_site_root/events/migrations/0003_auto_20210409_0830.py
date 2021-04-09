# Generated by Django 3.2 on 2021-04-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210407_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Web address'),
        ),
    ]
