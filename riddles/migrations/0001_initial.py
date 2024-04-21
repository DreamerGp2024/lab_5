# Generated by Django 5.0.4 on 2024-04-21 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('riddle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.riddle')),
            ],
        ),
    ]
