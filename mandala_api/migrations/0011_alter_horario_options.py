# Generated by Django 3.2.8 on 2021-11-30 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_api', '0010_auto_20211129_2150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={'ordering': ['dia']},
        ),
    ]
