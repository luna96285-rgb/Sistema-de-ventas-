from django import forms
from .models import Usuarios
from django.contrib.auth.models import User #Usamos el modelo de user para evitar hacer encriptacion de contra

#importaciones para requisitos para una contraseña segura
from django.contrib.auth.password_validation import validate_password #comprueba si una contraseña cumple las reglas de seguridad configuradas en Django.
from django.core.exceptions import ValidationError #Representa un error de validación que podemos capturar y mostrar al usuario.


class FormularioRegistroUsuario(forms.Form):
    
    #campos del regsitro
    
    #Nombre debe ser igual NAME= del campo del HTML
    nombre = forms.CharField(
        max_length=50,
        required=True,
        widget= forms.TextInput(attrs={
            'class' : 'input', #N ombre de la CLASS del Campo en HTML
            'id' : 'reg-nombre' # Nombre de ID en el campo de HTMl
        })
    )
    
    apellido = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class' : 'input',
            'id' : 'reg-apellido'
        })
    )
    
    correo = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'id': 'reg-correo'
        })
    )
    
    telefono = forms.CharField(
        max_length=10,
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class':'input',
            'id':'reg-telefono'
        })
    )
    
    password = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={ #ponemos PasswordInput para que aparesca la contraseña asi **********
            'class':'input',
            'id':'reg-password'
        })
    )
    
    password2 = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class':'input',
            'id':'reg-password2'
        })
    )

    #---------------------------    
    # VALIDACIONE DE INFORMACION
    
    # correo repetidos
    def clean_correo(self):
        correo_ingresado = self.cleaned_data.get('correo','').strip().lower()
        
        #Correo no repetidos
        if User.objects.filter(email=correo_ingresado).exists(): #Si en la tabla de auth_user hay un correo igual al que escribio el usuario muestra un error
            raise forms.ValidationError("Ya existe una cuenta existente con este correo")
        
        #Correo terminado en gmail o Hotmail
        if not correo_ingresado.endswith(('@gmail.com', '@hotmail.com')):
            raise forms.ValidationError("El correo debe ser @gmail.com o @hotmail.com")
        
        return correo_ingresado
    
    # telefono repetidos
    def clean_telefono(self):
        telefono_ingresado = self.cleaned_data.get('telefono')
        
        #No repetidos
        if Usuarios.objects.filter(telefono=telefono_ingresado).exists(): 
            raise forms.ValidationError("Ya existe una cuenta existente con este telefono")
        
        #Solo numeros
        if not telefono_ingresado.isdigit():
            raise forms.ValidationError("El numero de Telefono solo debe ser numerico")
        
        #Al menos 10 caracteres
        if len(telefono_ingresado) != 10:
            raise forms.ValidationError("EL numero debe tener 10 caracteres")
        
        #numero debe empezar por 3
        if not telefono_ingresado.startswith('3'):
            raise forms.ValidationError("El numero de Telefono debe empezar por 3 (colombia)")
        
        
        return telefono_ingresado
    
    
    #Las 2 contraseñas coincidan en el registro(NO USAMOS def clean_password PORQUE ESTO ES VALIDACIONES INDIVIDUALES PARA CADA CAMPO)
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        # Verificamos que las contraseñas coincidan
        if password and password2 and password != password2:
            self.add_error(
                'password2',
                'La confirmación de contraseña no coincide'
            )

        #Para que la contraseña cumpla con requisitos de seguridad
        if password:
            try:
                validate_password(password)
                
            except ValidationError as error: #Aqui los mensajes de errores ya viene integrados con ValidationError
                self.add_error(field='password', error=error)
            
        return cleaned_data
                    
    

# Formulario para inicio sesion 
class FormularioInicioSesion(forms.Form):
    
    correo = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'id' : 'login-correo'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class' : 'input',
            'id' : 'login-password'
        })
    )