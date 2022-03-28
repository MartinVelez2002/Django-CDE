from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def inicio(request):
    return render(request,"index.html")

# Vistas de Cargos

def cargo (request):
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request,"pages/cargo.html", {'cargoForm':cargo_form,'cargos':cargos,'accion':'Añadir Cargo'})

def crearCargo (request):
    if request.method == "POST":
        cargo_form = CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('cargo')
        # data['estado']=cargo_form
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request,"pages/agregarCargo.html", {'cargoForm':cargo_form,'cargos':cargos,'accion':'Crear'})
    
def editarCargo(request,id):
    error,cargo_form=None,None
    try:
        cargo = Cargo.objects.get(id=id)
        if request.method=="GET":
            cargo_form = CargoForm(instance=cargo)
        else:
            cargo_form = CargoForm(request.POST,instance=cargo)
            if cargo_form.is_valid():
                cargo_form.save()
                return redirect('cargo')
    except Exception as e:
        error=e
    cargos = Cargo.objects.all()
    return render(request,"pages/editarCargo.html", {'cargoForm':cargo_form,'cargos':cargos ,'accion':'Actualizar'})

def eliminarCargo(request,id):
    cargo = Cargo.objects.get(id=id)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo')
    return render(request,"pages/eliminarCargo.html", {'cargo':cargo})



# Vistas de Departamentos
def departamento (request):
    depar_form = DeparForm()
    departamento = Departamento.objects.all()
    return render(request,"pages/departamento.html", {'deparForm':depar_form,'depar':departamento,'accion':'Añadir Departamento'})


def crearDepar (request):
    if request.method == "POST":
        depar_form = DeparForm(request.POST)
        if depar_form.is_valid():
            depar_form.save()
            return redirect('departamento')
    depar_form = DeparForm()
    departamento = Departamento.objects.all()
    return render(request,"pages/agregarDepartamento.html", {'deparForm':depar_form,'depar':departamento,'accion':'Crear'})

def editarDepar(request,id):
    error,depar_form=None,None
    try:
        departamento = Departamento.objects.get(id=id)
        if request.method=="GET":
            depar_form = DeparForm(instance=departamento)
        else:
            depar_form = DeparForm(request.POST,instance=departamento)
            if depar_form.is_valid():
                depar_form.save()
                return redirect('departamento')
    except Exception as e:
        error=e
    
    departamento = Departamento.objects.all()
    return render(request,"pages/editarDepartamento.html", {'deparForm':depar_form,'depar':departamento ,'accion':'Actualizar'})


def eliminarDepar(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method=='POST':
        departamento.delete()
        return redirect('departamento')
    return render(request,'pages/eliminarDepar.html',{'departamento':departamento})




# Vistas de Empleados
def empleado (request):
    empleado_form = EmpleadoForm()
    emple = Empleado.objects.all()
    return render(request,"pages/empleado.html", {'empleadoForm':empleado_form,'empleados':emple ,'accion':'Añadir Empleado'})

def crearEmpleado(request):
    if request.method == "POST":
        empleado_form = EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('empleado')
    empleado_form = EmpleadoForm()
    emple = Empleado.objects.all()
    return render(request,"pages/agregarEmpleado.html", {'empleadoForm':empleado_form,'empleados':emple ,'accion':'Crear'})

def editarEmpleado(request,id):
    error,empleado_form=None,None
    try:
        empleados = Empleado.objects.get(id=id)
        if request.method=="GET":
            empleado_form = EmpleadoForm(instance=empleados)
        else:
            empleado_form = EmpleadoForm(request.POST,instance=empleados)
            if empleado_form.is_valid():
                empleado_form.save()
                return redirect('empleado')
    except Exception as e:
        error=e
    empleados = Empleado.objects.all()
    return render(request,"pages/editarEmpleado.html", {'empleadoForm':empleado_form,'empleados':empleados ,'accion':'Actualizar'})

def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado')

    return render(request,"pages/eliminarEmpleado.html",{'empleado':empleado})
