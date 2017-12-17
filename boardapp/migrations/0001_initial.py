# Generated by Django 2.0 on 2017-12-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('b_gender', models.CharField(default='m', max_length=2)),
                ('b_title', models.CharField(max_length=100)),
                ('b_time', models.DateTimeField(auto_now=True)),
                ('b_content', models.TextField()),
                ('b_response', models.TextField(blank=True, default='')),
            ],
        ),
    ]
