from django import forms
from django.forms import ModelForm
from .models import Proyecto

class ProyectoF(ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo','descripcion','url','imagen']

        read_only_fields = ['created_at']