# Generated by Django 3.2.8 on 2021-11-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_api', '0009_clase_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='aficiones',
            field=models.ManyToManyField(blank=True, to='mandala_api.Aficion'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(choices=[('L', 'Lunes'), ('M', 'Martes'), ('A', 'Miércoles'), ('J', 'Jueves'), ('V', 'Viernes')], max_length=1),
        ),
    ]