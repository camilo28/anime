from django import forms 
from anime.models import Demonio,ParteDelCuerpo,Ciudad,Personaje,Articulo,ResultadoPelea,Pelea
class DemonioForm(forms.ModelForm):
    partedelcuerpo=forms.ModelChoiceField(
        queryset=ParteDelCuerpo.objects.order_by('id')
    )
    ciudad=forms.ModelChoiceField(
        queryset=Ciudad.objects.order_by('id')
    )
    class Meta:
        model=Demonio
        fields=['partedelcuerpo','ciudad','nombre']
        labels={'partedelcuerpo':"Parte Del Cuerpo",'ciudad':'Ciudad','nombre':"Nombre Demonio"}
        widget={'nombre':forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })       
    
class ParteForm(forms.ModelForm):
    class Meta:
        model=ParteDelCuerpo
        fields=['nombre']
        labels={'nombre':"Nombre Parte Del Cuerpo"}
        widget={'nombre':forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })  

class CiudadForm(forms.ModelForm):
    class Meta:
        model=Ciudad
        fields=['nombre']
        labels={'nombre':"Nombre Ciudad"}
        widget={'nombre':forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })            
class PersonajeForm(forms.ModelForm):
    class Meta:
        model=Personaje
        fields=['nombre']
        labels={'nombre':"Nombre Personaje"}
        widget={'nombre':forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })     

class ArticuloForm(forms.ModelForm):
    personaje=forms.ModelChoiceField(
        queryset=Personaje.objects.order_by('id')
    )
    class Meta:
        model=Articulo
        fields=['nombre','personaje']
        labels={'nombre':"Nombre Articulo",'personaje':'Propietario'}
        widget={'nombre':forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })    
                
class ResultadoForm(forms.ModelForm):
    class Meta:
        model=ResultadoPelea
        fields=['nombre']
        labels={'nombre':"Resultado"}
        widget={'nombre':forms.TextInput()}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })            

class PeleaForm(forms.ModelForm):
    personaje=forms.ModelChoiceField(
        queryset=Personaje.objects.order_by('id')
    )
    demonio=forms.ModelChoiceField(
        queryset=Demonio.objects.order_by('id')
    )
    resultadopelea=forms.ModelChoiceField(
        queryset=ResultadoPelea.objects.order_by('id')
    )
    class Meta:
        model=Pelea
        fields=['personaje','demonio','resultadopelea']
        labels={'personaje':"Personaje Involucrado",'demonio':"Demonio Involucrado",'resultadopelea':'Estado Pelea'}
        widget={}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
            'class': 'form-control'
        })    

