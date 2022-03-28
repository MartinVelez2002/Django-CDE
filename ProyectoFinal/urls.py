"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mtto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="inicio"),
# /-------------------------------------------------------------------------/ #

    path('cargo/',cargo, name="cargo" ),
    path('agregarCargo/',crearCargo, name="agregarCargo" ),
    path('editarCargo/<int:id>',editarCargo, name="editarCargo" ),
    path('eliminarCargo/<int:id>',eliminarCargo, name="eliminarCargo" ),

# /-------------------------------------------------------------------------/ #

    path('departamento/',departamento, name="departamento" ),
    path('agregarDepartamento/',crearDepar, name="agregarDepartamento" ),
    path('editarDepar/<int:id>',editarDepar, name="editarDepar" ),
    path('eliminarDepar/<int:id>',eliminarDepar, name="eliminarDepar" ),

# /-------------------------------------------------------------------------/ #

    path('empleado/',empleado, name="empleado" ),
    path('agregarEmpleado/',crearEmpleado, name="agregarEmpleado"),
    path('editarEmpleado/<int:id>',editarEmpleado, name="editarEmpleado"),
    path('eliminarEmpleado/<int:id>',eliminarEmpleado, name="eliminarEmpleado"),

]
