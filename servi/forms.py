from django import forms
from.models import Cita

class CitaForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cita
        fields =["nombre","email","modelo","patente","marca","servicio","fecha","precio"]
        #fields = '__all__'