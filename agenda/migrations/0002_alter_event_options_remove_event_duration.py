# Generated by Django 4.2.16 on 2024-10-19 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='duration',
        ),
    ]
