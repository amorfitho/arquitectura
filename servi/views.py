from django.shortcuts import render

# Create your views here.

#
def main(request):
    return render(request, 'servi/main.html')
#
def login(request):
    return render(request, 'servi/login.html')
#
def regsitro(request):
    return render(request, 'servi/registro.html')
#
def reservas(request):
    return render(request, 'servi/reservas.html')
#
def reservas2(request):
    return render(request, 'servi/reservas2.html')
#
def servicios(request):
    return render(request, 'servi/servicios.html')
#
def productos(request):
    return render(request, 'servi/productos.html')
#
def empleados(request):
    return render(request, 'servi/empleados.html')
#
def horarios(request):
    return render(request, 'servi/horarios.html')
#
#
#
