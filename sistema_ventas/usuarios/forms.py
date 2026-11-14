from django import forms
from .models import Usuarios
from django.contrib.auth.models import User #Usamos el modelo de user para evitar hacer encriptacion de contra

class FormularioRegistroUsuario(forms.Form):
    
    #campos del regsitro
    
    #Nombre debe ser igual NAME= del campo del HTML
    nombre = forms.CharField(
        max_length=50,
        required=True,
        widget= forms.TextInput(attrs={
            'class' : '', #N ombre de la CLASS del Campo en HTML
            'id' : '' # Nombre de ID en el campo de HTMl
        })
    )
    
    apellido = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class' : '',
            'id' : ''
        })
    )
    
    correo = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': '',
            'id': ''
        })
    )
    
    telefono = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'',
            'id':''
        })
    )
    
    password = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'',
            'id':''
        })
    )
    
    password_confirm = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'',
            'id':''
        })
    )

    #---------------------------    
    # VALIDACIONE DE INFORMACION
    
    # correo repetidos
    def clean_correo(self):
        correo_ingresado = self.cleaned_data.get('correo')
        
        if User.objects.filter(email=correo_ingresado).exists(): #Si en la tabla de auth_user hay un correo igual al que escribio el usuario muestra un error
            raise forms.ValidationError("Ya existe una cuenta existente con este correo")
        
        return correo_ingresado
    
    # telefono repetidos
    def clean_telefono(self):
        telefono_ingresado = self.cleaned_data.get('telefono')
        
        if Usuarios.objects.filter(telefono=telefono_ingresado).exists(): 
            raise forms.ValidationError("Ya existe una cuenta existente con este telefono")
        
        return telefono_ingresado