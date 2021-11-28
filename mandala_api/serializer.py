from .models import *
from rest_framework import serializers

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las peticiones para Plan"""

    class Meta:
        model = Plan
        fields = ('id', 'nombre', 'descripcion', 'costo', 'horarios')

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las peticiones para Instructor"""

    planes = PlanSerializer(many=True, read_only=True)

    class Meta:
        model = Horario
        fields = ('dia', 'hora_inicio', 'hora_fin', 'clase', 'planes')

class ClaseSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las peticiones para Plan"""

    horarios = HorarioSerializer(many=True, read_only=True)

    class Meta:
        model = Clase
        fields = ('id', 'nombre', 'descripcion', 'instructor', 'horarios', 'horarios_clase')

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las peticiones para Instructor"""

    clases = ClaseSerializer(many=True, read_only=True)

    class Meta:
        model = Instructor
        fields = ('id', 'nombre', 'apellido', 'descripcion', 'clases', 'clases_instructor')
