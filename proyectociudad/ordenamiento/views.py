from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render


# Importar las clases de models.py
from ordenamiento.models import *

# Importar los formularios de forms.py
from ordenamiento.forms import *

# Create your views here.

# - Generar una vista que liste las parroquias y sus barrios
# - Generar una vista que liste los barrios
# - Generar un formulario que cree una parroquia
# - Generar un formulario que cree un barrio de una parroquia
# - Generar un formulario que edite una parroquia
# - Generar un formulario que edite un barrio




def index(request):

    parroquias = Parroquia.objects.all()

    informacion_template = {'parroquias': parroquias,
                            'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)


# - Generar una vista que liste las parroquias y sus barrioss

def obtener_parroquia(request, id):

    parroquias = Parroquia.objects.get(pk=id)

    informacion_template = {'parroquias': parroquias}
    return render(request, 'obtenerParroquia.html', informacion_template)

# - Generar una vista que liste los barrios
def obtener_barrio(request, id):

    barrios = Barrio.objects.get(pk=id)

    informacion_template = {'barrios': barrios}
    return render(request, 'obtenerBarrios.html', informacion_template)

# - Generar un formulario que cree una parroquia

def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)

# - Generar un formulario que edite una parroquia


def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)

# - Generar un formulario que cree un barrio de una parroquia


def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crearBarrio.html', diccionario)

# - Generar un formulario que edite un barrio


def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)
