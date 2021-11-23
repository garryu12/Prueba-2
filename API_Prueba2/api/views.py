import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import  Alumnos


# Create your views here.
 
class AlumnosView(View):

    @method_decorator(csrf_exempt)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,correo):
        try:
            alumnos=list(Alumnos.objects.filter(correo=correo).values())
            if len(alumnos) > 0:
                alumno=alumnos[0]
                datos = {'message':"Success",'alumno':alumno}
            else:
                datos={'message':"Alumno no encontrado..."}
            return JsonResponse(datos)

        except:
            alumnos=list(Alumnos.objects.values())
            if len(alumnos)>0:
                datos={'message':"Success",'alumnos':alumnos}
            else:
                datos={'message':"Alumno no encontrado..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        Alumnos.objects.create(nombreAlumno=jd['nombre_alumno'],correoAlumno=jd['correo_alumno'],passwordAlumno=jd['password_alumno'])
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass
