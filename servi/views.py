from django.shortcuts import render
from .forms import CitaForm

# Create your views here.

#--------------------------------------------------------------------------------------------------
def main(request):
    return render(request, 'servi/main.html')
#--------------------------------------------------------------------------------------------------
def login(request):
    return render(request, 'registration/login.html')
#--------------------------------------------------------------------------------------------------
def registro(request):
    return render(request, 'registration/registro.html')
#--------------------------------------------------------------------------------------------------
def reservas(request):
    return render(request, 'servi/reserv/reservas.html')
#--------------------------------------------------------------------------------------------------
def reservas2(request):
    return render(request, 'servi/reserv/reservas2.html')
#--------------------------------------------------------------------------------------------------
def servicios(request):
    return render(request, 'servi/serv/servicios.html')
#--------------------------------------------------------------------------------------------------
def productos(request):
    return render(request, 'servi/serv/productos.html')
#--------------------------------------------------------------------------------------------------
def empleado(request):
    return render(request, 'servi/serv/empleado.html')
#--------------------------------------------------------------------------------------------------
def horarios(request):

    data={
        'form': CitaForm()
    }

    if request.method== 'POST':
        formulario = CitaForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data ["from"] = formulario

    return render(request, 'servi/serv/horarios.html', data )
#--------------------------------------------------------------------------------------------------
#
#
