from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from api.models import Alumnos


class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ['nombre_alumnno', 'correo_alumno', 'password_alumno']