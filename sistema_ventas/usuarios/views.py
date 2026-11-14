from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User #importamos para guardar los datos a la tabla de auth_user
from .forms import FormularioRegistroUsuario
from .models import Usuarios # importamos para guardar los datos a la tabla de usuarios

# Create your views here.

def registroUsuario(request):
    
    if request.method == 'POST':
        
        formulario = FormularioRegistroUsuario(request.POST)
        
        if formulario.is_valid():
                
                #extraemos los datos para ingresar a la tabla de AUTH_USER
                nombre = formulario.cleaned_data.get('nombre')
                apellido = formulario.cleaned_data.get('apellido')
                correo = formulario.cleaned_data.get('correo')
                password = formulario.cleaned_data.get('password')
                
                #verficamos que la password sea igual a la confirmacion de password_confirm
                if password != formulario.cleaned_data.get('password_confirm'):
                    messages.error(request, 'La contraseña no coinciden')
                    
                    return render(request, '', {
                        'formulario' : formulario # Le devolvemos el formulario para que lo corriga
                    })             
                    
                #Introducimos los datos a la tabla de AUTH_USER
                try:
                    nuevo_usuario = User.objects.create_user(
                    
                        username=correo, #Username es obligatoria, pero como no tenemos el campo de usarname en el formulario le asignamos es correo
                        first_name=nombre,
                        last_name=apellido,
                        password=password
                    )
                    
                except Exception as e:
                    messages.error(request, 'Error al crear la cuenta. Intentalo mas tarde')
                    
                    return render(request, '', {
                        'formulario' : formulario
                    })
                    
                #Introducimos los datos a la tabla de usuario
                try:
                    Usuarios.objects.create(
                        nombre=formulario.cleaned_data.get('nombre'),
                        apellido=formulario.cleaned_data.get('apellido'),
                        telefono=formulario.cleaned_data.get('correo'),
                        id_usuario_fk=nuevo_usuario #Usamos la variable donde se creo el asuario para introducirlo a la tabla de auth_user
                    )
                    
                    messages.success(request, f'!!Hola, Bienvendo {nuevo_usuario.nombre}')
                    return redirect('')
                
                except Exception as e:
                    #si falla el registro, eliminamos el usuario base para no dejar datos huerfanos
                    nuevo_usuario.delete()
                    messages.error(request, "Hubo un error intentalo de nuevo")
                    
                    return render(request, '', {
                        'formulario' : formulario
                    })
        
        else:
            messages.error(request, 'No cumple con los requistos del formulario')
            
    else:
        #si la peticion es GET(Entra por primera vez a la pagina)
        formulario = FormularioRegistroUsuario() #decimos que el formulario se lo vamos a entregar vacio
        
        return render(request, '', {
            'formulario' : formulario #le pasamos el formulario para que lo llene
        })        
        