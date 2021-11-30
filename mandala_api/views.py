from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework import serializers
from .serializer import *
from django.http import JsonResponse, HttpResponse

# Create your views here.

class PlanViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Plan"""
   queryset = Plan.objects.all().order_by('id')
   serializer_class = PlanSerializer

class InstructorViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Instructor"""
   queryset = Instructor.objects.all().order_by('nombre')
   serializer_class = InstructorSerializer

class ClaseViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Clase"""
   queryset = Clase.objects.all().order_by('nombre')
   serializer_class = ClaseSerializer

class HorarioViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Horario"""
   queryset = Horario.objects.all().order_by('id')
   serializer_class = HorarioSerializer

class AficionViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Aficion"""
   queryset = Aficion.objects.all().order_by('nombre')
   serializer_class = AficionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
   """API que permite realizar operaciones en la tabla Cliente"""
   queryset = Cliente.objects.all().order_by('id')
   serializer_class = ClienteSerializer

def planDetail(request, idPlan):
   plan = Plan.objects.get(pk = idPlan)

   horario = []

   for p in plan.horarios.all():
      horario.append({'dia': p.dia, 'inicio' : p.hora_inicio, 'fin' : p.hora_fin, 'clase' : p.clase.nombre, 'instructor' : p.clase.instructor.nombre + " " + p.clase.instructor.apellido, 'img': p.clase.instructor.img})

   response_data = {}
   response_data['plan'] = {'nombre': plan.nombre, 'costo': plan.costo, 'descripcion': plan.descripcion }
   response_data['horario'] = horario

   return JsonResponse(response_data)

def instructorDetail(request, idInstructor):
   instructor = Instructor.objects.get(pk = idInstructor)

   clases = []

   for c in instructor.clases_instructor.all().order_by('nombre'):
      clases.append({'clase': c.nombre})

   response_data = {}
   response_data['instructor'] = {'nombre': instructor.nombre, 'apellido': instructor.apellido, 'descripcion': instructor.descripcion, 'img': instructor.img }
   response_data['clases'] = clases

   return JsonResponse(response_data)

def claseDetail(request, idClase):
   clase = Clase.objects.get(pk = idClase)

   response_data = {}
   response_data['clase'] = {'nombre': clase.nombre, 'descripcion': clase.descripcion, 'instructor': clase.instructor.nombre + " " + clase.instructor.apellido, 'img' : clase.img }
   
   return JsonResponse(response_data)


