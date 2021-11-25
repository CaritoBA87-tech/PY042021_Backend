from django.contrib import admin
from .models import Plan, Horario, Instructor, Clase

# Register your models here.

admin.site.register(Plan)
admin.site.register(Horario)
admin.site.register(Instructor)
admin.site.register(Clase)
