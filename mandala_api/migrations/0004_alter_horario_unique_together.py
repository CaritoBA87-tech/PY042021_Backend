# Generated by Django 3.2.9 on 2021-11-20 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_api', '0003_rename_clase_plan_horarios'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together={('hora_inicio', 'hora_fin', 'dia', 'clase')},
        ),
    ]
