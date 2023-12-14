from django.forms import ModelForm
from django import forms
from .models import Usuario

class usuariosform(forms.ModelForm):
    class Meta:
        model = Usuario
        #fields = ['nombre_paciente','nombre_doc', 'fechayhora'] 
   
        fields = '__all__' 