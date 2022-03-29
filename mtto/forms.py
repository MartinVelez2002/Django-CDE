from django import forms 
from .models import *

class CargoForm(forms.ModelForm):
    class Meta: 
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Descripción del Cargo',
                'class':'form-group',
                'required': True,

            })
            
        }
        
class DeparForm(forms.ModelForm):
    class Meta: 
        model = Departamento
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Descripción del Departamento',
                'class':'form-group',
                'required': True

            })
            
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre','cedula','cargo','departamento','sueldo','estado']
        widgets = {
            'nombre':forms.TextInput(attrs={
                'placeholder':'Nombre del Empleado',
                'class':'form-group',
                'required': True
            }),
            
            'cedula':forms.NumberInput(attrs={
                'placeholder':'Digite su número de cédula',
                'class':'form-group',
                'required': True
            }),

            'cargo':forms.Select(attrs={
                'class':'form-group',
                'required': True
            }),

            'departamento':forms.Select(attrs={
            'class':'form-group',
            'required': True
            }),

            'sueldo':forms.NumberInput(attrs={
                'placeholder':'Sueldo del Empleado',
                'class':'form-group',
                'required':True
            })
        } 
