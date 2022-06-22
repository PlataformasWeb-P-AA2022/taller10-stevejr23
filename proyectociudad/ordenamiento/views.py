from django.shortcuts import render

# Create your views here.

# Importar las clases de models.py
from ordenamiento.models import *

# Importar los formularios de forms.py
from ordenamiento.forms import *

def index(request):

    parroquias = Parroquia.objects.all()

    informacion_template = {'parroquia': parroquias, 'numero_parroquias': len(parroquias)}
    return render (request, 'index.html',informacion_template)
    