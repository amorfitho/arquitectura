from django import forms
from.models import Cita
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserModel

class CitaForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cita
        fields =["nombre","email","modelo","patente","marca","servicio","fecha","precio"]
        #fields = '__all__'

        widgets = {
            "fecha" : forms.SelectDateWidget()
        }

class CustomUser(UserCreationForm):
    pass

