import json
from django.db.models import expressions
from django.http import request, response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from api.serializers import AlumnosSerializers


from .models import  Alumnos


# Create your views here.
 
class AlumnosView(View):

    @csrf_exempt
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, correo_alumno):
        try:
            alumnos=list(Alumnos.objects.filter(correo_alumno=correo_alumno).values())
            if len(alumnos) > 0:
                alumno=alumnos[0]
                datos = {'message':"Success",'alumno':alumno}
            else:
                datos={'message':"Alumno no encontrado..."}
            return JsonResponse(datos)

        except:
            alumnos=list(Alumnos.objects.values())
            if len(alumnos)>0:
                datos={'message': "Success",'alumnos':alumnos}
            else:
                datos={'message':"Alumno no encontrado..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        Alumnos.objects.create(nombre_alumnno=jd['nombre_alumnno'],correo_alumno=jd['correo_alumno'],password_alumno=jd['password_alumno'])
        datos={'message': "Success"}
        return JsonResponse(datos)




@api_view(['PUT'])
def putAlumno(request, correo_alumno):
    jd = json.loads(request.body)
    alumnos = list(Alumnos.objects.filter(correo_alumno=correo_alumno).values())
    if len(alumnos) > 0:
        alumno=Alumnos.objects.get(correo_alumno=correo_alumno)
        alumno.correo_alumno=jd['correo_alumno']
        alumno.password_alumno=jd['password_alumno']
        alumno.save()
        datos={'message': "Success"}

    else:
        datos={'message':"Alumno no encontrado..."}
    return JsonResponse(datos)

@api_view(['DELETE'])
def deleteAlumno(request, correo_alumno):
    try:
        alumno = Alumnos.objects.get(correo_alumno=correo_alumno)
    except Alumnos.DoesNotExist:
        datos={'message':"Alumno no encontrado..."}
        return JsonResponse(datos)
    if request.method=='DELETE':
        alumno.delete()
        datos={'message': "Success"}
    return JsonResponse(datos)

@api_view(['GET'])
def loginUsuario(request, correo_alumno, password_alumno):     
    try:         
        usuario = Alumnos.objects.get(correo_alumno=correo_alumno, password_alumno=password_alumno)     
    except Alumnos.DoesNotExist:         
        datos={'message':"Alumno no encontrado..."}
        return JsonResponse(datos)
    if request.method=='GET':         
        serializer = AlumnosSerializers(usuario)  
        datos={'message': "Success"}       
        return JsonResponse(serializer.data)     
    else:          
        datos={'message':"Alumno no encontrado..."}
        return JsonResponse(datos)