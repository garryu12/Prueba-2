from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import  Alumnos

# Create your views here.
 
class AlumnosView(View):

    def get(self, request):
        alumnos=list(Alumnos.objects.values())
        if len(alumnos)>0:
            datos={'message':"Success",'alumnos':alumnos}
        else:
            datos={'message':"Alumno no encontrado..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
