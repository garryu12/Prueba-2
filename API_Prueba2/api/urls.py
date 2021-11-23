from django.urls import path
from api.views import AlumnosView, putAlumno, deleteAlumno, loginUsuario


urlpatterns=[
    path('alumnos/', AlumnosView.as_view(), name='alumnos_list'),
    path('alumnos/<correo_alumno>', AlumnosView.as_view(), name='alumnos_process'),
    path('putAlumno/<correo_alumno>', putAlumno, name='putAlumno'),
    path('deleteAlumno/<correo_alumno>', deleteAlumno, name='deleteAlumno'),
    path('loginUsuario/<correo_alumno>/<password_alumno>', loginUsuario, name='loginUsuario')
]