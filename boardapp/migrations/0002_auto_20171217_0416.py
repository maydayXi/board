# Generated by Django 2.0 on 2017-12-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardunit',
            name='b_mail',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='boardunit',
            name='b_web',
            field=models.URLField(blank=True, default=''),
        ),
    ]
