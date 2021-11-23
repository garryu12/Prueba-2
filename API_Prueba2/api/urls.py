from django.urls import path
from .views import AlumnosView


urlpatterns=[
    path('alumnos/', AlumnosView.as_view(), name='alumnos_list'),
    path('alumnos/<correo>', AlumnosView.as_view(), name='alumnos_process')
]