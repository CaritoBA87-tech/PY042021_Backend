from django.db import models

# Create your models here.

class Instructor(models.Model):
    """ Define el modelo Instructor """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        """ Se define la representación en str para Instructor """
        return "{} {}".format(self.nombre, self.apellido) 

class Clase(models.Model):
    """ Define el modelo Clase """
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name="clases_instructor")

    def __str__(self):
        return "{}".format(self.nombre) 

class Horario(models.Model):
    """ Define el modelo Horario """

    class Meta:
        unique_together = (('hora_inicio', 'hora_fin', 'dia', 'clase'),)

    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    DIA = [("L", "Lunes"),("M", "Martes"), ("N", "Miércoles"),("J", "Jueves"), ("V", "Viernes")]

    dia = models.CharField(max_length=1, choices=DIA)
    clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True, related_name="horarios_clase")

    def __str__(self):
        """ Se define la representación en str para Horario """
        return "{} {} {} {}".format(self. dia, self.hora_inicio, self.hora_fin, self.clase) 

class Plan(models.Model):
    """ Define el modelo Plan """
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    horarios = models.ManyToManyField(Horario)

    def __str__(self):
        """ Se define la representación en str para Plan """
        return "{} {} {}".format(self.id, self. nombre, self.costo) 
