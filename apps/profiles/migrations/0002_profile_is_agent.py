# Generated by Django 3.2.7 on 2022-11-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_agent',
            field=models.BooleanField(default=False, help_text='Are you an agent?', verbose_name='Agent'),
        ),
    ]
