from django.urls import path
from .views import main, login, registro, reservas, reservas2,servicios, productos, empleados, horarios

urlpatterns = [
    path('', main, name="main"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('reservas/', reservas, name="reservas"),
    path('reservas2/', reservas2, name="reservas2"),
    path('servicios/', servicios, name="servicios"),
    path('productos/', productos, name="productos"),
    path('empleados/', empleados, name="empleados"),
    path('horarios/', horarios, name="horarios"),

]