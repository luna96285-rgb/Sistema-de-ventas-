from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User #importamos para guardar los datos a la tabla de auth_user
from .forms import FormularioRegistroUsuario, FormularioInicioSesion
from .models import Usuarios # importamos para guardar los datos a la tabla de usuarios
from django.contrib.auth import authenticate, login, logout #Importamos las acciones para hacer la ATHENTICATE de la  contraseña hacer LOGIN Y LOGOUT
from django.views.decorators.http import require_POST

# Create your views here.
# (REQUEST : NOS PERMITE HACER PETICIONES A INTERNED OSEA AL NAVEGADOR)

def registroUsuario(request):
    
    if request.method == 'POST':
        
        formulario = FormularioRegistroUsuario(request.POST)
        
        if formulario.is_valid():
                
            #extraemos los datos para ingresar a la tabla de AUTH_USER
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            correo = formulario.cleaned_data.get('correo')
            password = formulario.cleaned_data.get('password')
                     
                    
            #Introducimos los datos a la tabla de AUTH_USER
            try:
                nuevo_usuario = User.objects.create_user(
                    
                    username=correo, #Username es obligatoria, pero como no tenemos el campo de usarname en el formulario le asignamos es correo
                    first_name=nombre,
                    last_name=apellido,
                    email=correo,
                    password=password
                )
                    
            except Exception as e:
                messages.error(request, 'Error al crear la cuenta. Intentalo mas tarde')
                    
                return render(request, 'cuentas/registro.html', {
                    'formulario' : formulario
                })
                    
            #Introducimos los datos a la tabla de usuario
            try:
                Usuarios.objects.create(
                    nombre=formulario.cleaned_data.get('nombre'),
                    apellido=formulario.cleaned_data.get('apellido'),
                    telefono=formulario.cleaned_data.get('telefono'),
                    id_usuario_fk=nuevo_usuario #Usamos la variable donde se creo el usuario para introducirlo a la tabla de auth_user
                )
                    
                messages.success(request, f'!!Hola, Bienvendo {nombre}')
                return redirect('login')
                
            except Exception as e:
                #si falla el registro, eliminamos el usuario base para no dejar datos huerfanos
                nuevo_usuario.delete()
                messages.error(request, "Hubo un error intentalo de nuevo")
                    
                return render(request, 'cuentas/registro.html', {
                    'formulario' : formulario
                })
        
        else:
            #Esto es para que no salgan los mensajes de LAS VALICACIONES DEL FORMS.PY (este el else de is_valid() Si alguna validacion salio mal muestra los mensajes de las raise del las valicaciones del FORMS.py)
            for campo, errores in formulario.errors.items():
                for error in errores:
                    messages.error(request, error)
            
    else:
        #si la peticion es GET(Entra por primera vez a la pagina)
        formulario = FormularioRegistroUsuario() #decimos que el formulario se lo vamos a entregar vacio
        
    return render(request, 'cuentas/registro.html', {
        'formulario' : formulario #le pasamos el formulario para que lo llene
    })        
        
        

#-------------------------------------------------------------------------------------------
def inicioSesion(request):
    
    if request.method == 'POST':
        formulario = FormularioInicioSesion(request.POST)
        
        #condicional para verificar las condiciones
        if formulario.is_valid():
            
            correo_ingresado = formulario.cleaned_data.get('correo')
            password_ingresada = formulario.cleaned_data.get('password')
            
            
            #Como la autenticacion de Django es por Username y contraseña
            # Y vamos ahacer la verificacion por correo, entonses remplazamos y ponemos que username es igual al correo
            usuario_autenticado = authenticate(request, username=correo_ingresado, password=password_ingresada)
            
            
            # con  el condicional vareficamos si el correo y contraseña coinciden y los mandan al login
            if usuario_autenticado is not None:
                login(request, usuario_autenticado) #la función login de Django, la cual crea oficialmente la sesión del usuario en el navegador
                messages.success(request, f"BIENVENIDO {usuario_autenticado.first_name} A TIENDA PARIS")
                return redirect('registro-usuarios')
                
            else:
                messages.error(request, "Correo o Contraseña incorrrecta!! 🤔")
                
                return render(request, 'cuentas/login.html', {
                    'formularioI' : formulario #Devolvemos el formulario con la informacion para que corriga
                })
            
            
        else:
            messages.error(request, "Upss !Hubo un error!")
    
    else:
        formulario = FormularioInicioSesion()
        
    return render(request, 'cuentas/login.html', {
        'formularioI' : formulario
    })
    
    

@require_POST #permite que esta vista se ejecute únicamente mediante una petición POST.
def cerrarSesion(request):
    
    logout(request)
    messages.success(request, "Has cerrado sesion !Hasta la proxima!😉")
    
    redirect('login')