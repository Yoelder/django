from django.contrib import admin
from django.urls import path
from app1 import views
from django.contrib.auth.views import LoginView, LogoutView
from app1.views import manage,services,home,registrar,editar,editarcu,eliminar,enviar_correo,formulario
from django.contrib.auth.decorators import login_required

from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),# url login
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('manage/', login_required(manage), name='manage'),# url mange

    path('cerrar/', views.cerrar, name='cerrar'),# cerrar sesion
    path("services/",services),
    path("home/",home),

    path('registrar/',registrar, name='registrar'),  # cerrar sesion
    path("eliminar/<codigo>", eliminar,name='eliminar'),
    path("editarcu/<codigo>", editarcu,name='editarcu'),
    path("editar/", editar,name='editar'),

    path("formulario/contactar/", enviar_correo,name='contactar'),
    path("formulario/",formulario,name='formulario'),
    ]

