from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout ,login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LogoutView
from datetime import datetime

from django.db.models import Q
# views.py


from app1.models import Curso

from django.http import JsonResponse




@login_required
def manage(request):
    fecha = datetime.now()
    fecha = fecha.strftime('%Y-%m-%d')
    busqueda=request.POST.get("Buscar")
    #busqueda=''
    #print(request.POST)
   #print(busqueda)
    #messages.success(request,'Elementos listados')
    curso = Curso.objects.all()
    if busqueda:
        curso=Curso.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(fecha__icontains=busqueda)|
            Q(credito__icontains=busqueda)

        ).distinct()
    else:
        None
    return render(request, 'manage.html', {"cursos": curso,"fecha": fecha})


def home(request):
    return render(request, 'home.html')

def services(request):# primera vista
    return render(request,"services.html")

def cerrar(request):
    logout(request)
    return redirect('login')
# Create your views here.







def registrar(request):
    #fecha = datetime.now()
    #fecha = fecha.strftime('%Y-%m-%d')
    # print(request.POST)
    fecha=request.POST['txtFecha']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']
    curso = Curso.objects.create(fecha=fecha, nombre=nombre, credito=credito)
    return redirect('manage')


def eliminar(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Elemento Eliminado')
    return redirect('manage')


def editarcu(request, codigo):

    curso = Curso.objects.get(codigo=codigo)

    return render(request, 'editar.html', {"cursos": curso})


def editar(request):
    fecha = request.POST['txtFecha']
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    credito = request.POST['numCreditos']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.credito = credito
    curso.fecha = fecha
    curso.save()
    return redirect('manage')




from django.core.mail import send_mail
from django.http import HttpResponse

def enviar_correo(request):
    print(request.POST)
    if request.method == 'POST':
        asunto = request.POST['txtAsunto']
        mail=request.POST['txtEmail']
        mensaje = request.POST['txtMensaje']+"\ncorreo: "+mail
        # Dirección de correo electrónico desde la que se enviará el correo
        correo_desde = 'yoelderrf@gmail.com'

        # Lista de destinatarios
        destinatarios = ['yoelder996@gmail.com']

        # Enviar correo
        send_mail(asunto, mensaje, correo_desde, destinatarios,fail_silently=False)

        # Puedes redirigir a una página de éxito o realizar otras acciones después de enviar el correo
        return redirect('formulario')
    #print(request.method)
    return HttpResponse(request,'Error.')

def formulario(request):
    print(request.POST)
    return render(request,'email2.html')

