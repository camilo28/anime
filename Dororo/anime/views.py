from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import  HttpResponse
from anime.models import Demonio,ParteDelCuerpo,Ciudad,Personaje,Articulo,ResultadoPelea,Pelea
from anime.form import DemonioForm,ParteForm,CiudadForm,PersonajeForm,ArticuloForm,ResultadoForm,PeleaForm


# Create your views here.

#VISTAS
class DemonioView(generic.ListView):
    model=Demonio
    template_name="anime/demonio_List.html"
    context_object_name="obj"

class ParteView(generic.ListView):
    model=ParteDelCuerpo
    template_name="anime/parte_List.html"
    context_object_name="parte"

class CiudadView(generic.ListView):
    model=Ciudad
    template_name="anime/ciudad_List.html"
    context_object_name='ciudad'

class PersonajeView(generic.ListView):
    model=Personaje
    template_name="anime/personaje_List.html"
    context_object_name='personaje'

class ArticuloView(generic.ListView):
    model=Articulo
    template_name="anime/articulo_List.html"
    context_object_name='articulo'

class ResultadoPeleaView(generic.ListView):
    model=ResultadoPelea
    template_name="anime/resultado_pelea_List.html"
    context_object_name='resultado'

class PeleaView(generic.ListView):
    model=Pelea
    template_name="anime/pelea_List.html"
    context_object_name='pelea'

#INSERCIONES
class DemonioInsert(generic.CreateView):
    model=Demonio
    template_name="anime/demonio_Insert.html"
    context_object_name="obj"
    form_class=DemonioForm
    success_url=reverse_lazy("anime:insertar_demonio")

class ParteInsert(generic.CreateView):
    model=ParteDelCuerpo
    template_name="anime/parte_Insert.html"
    context_object_name="parte"
    form_class=ParteForm
    success_url=reverse_lazy("anime:insertar_parte")

class CiudadInsert(generic.CreateView):
    model=Ciudad
    template_name="anime/ciudad_Insert.html"
    context_object_name="ciudad"
    form_class=CiudadForm
    success_url=reverse_lazy("anime:insertar_ciudad")

class PersonajeInsert(generic.CreateView):
    model=Personaje
    template_name="anime/personaje_Insert.html"
    context_object_name="personaje"
    form_class=PersonajeForm
    success_url=reverse_lazy("anime:insertar_personaje")    

class ArticuloInsert(generic.CreateView):
    model=Articulo
    template_name="anime/articulo_Insert.html"
    context_object_name="articulo"
    form_class=ArticuloForm
    success_url=reverse_lazy("anime:insertar_articulo")  
    
class ResultadoPeleaInsert(generic.CreateView):
    model=ResultadoPelea
    template_name="anime/resultado_pelea_Insert.html"
    context_object_name="resultado"
    form_class=ResultadoForm
    success_url=reverse_lazy("anime:insertar_resultado")        

class PeleaInsert(generic.CreateView):
    model=Pelea
    template_name="anime/pelea_Insert.html"
    context_object_name="pelea"
    form_class=PeleaForm
    success_url=reverse_lazy("anime:insertar_pelea")  

#EDICIONES
class DemonioEdit(generic.UpdateView):
    model=Demonio
    template_name="anime/demonio_Insert.html"
    context_object_name="obj"
    form_class=DemonioForm
    success_url=reverse_lazy("anime:listar_demonio")  

class ParteEdit(generic.UpdateView):
    model=ParteDelCuerpo
    template_name="anime/parte_Insert.html"
    context_object_name="parte"
    form_class=ParteForm
    success_url=reverse_lazy("anime:listar_parte")

class CiudadEdit(generic.UpdateView):
    model=Ciudad
    template_name="anime/ciudad_Insert.html"
    context_object_name="ciudad"
    form_class=CiudadForm
    success_url=reverse_lazy("anime:listar_ciudad")  

class PersonajeEdit(generic.UpdateView):  
    model=Personaje
    template_name="anime/personaje_Insert.html"
    context_object_name="personaje"
    form_class=PersonajeForm
    success_url=reverse_lazy("anime:listar_personaje")    

class ArticuloEdit(generic.UpdateView):  
    model=Articulo
    template_name="anime/articulo_Insert.html"
    context_object_name="articulo"
    form_class=ArticuloForm
    success_url=reverse_lazy("anime:listar_articulo")   

class ResultadoPeleaEdit(generic.UpdateView):
    model=ResultadoPelea
    template_name="anime/resultado_pelea_Insert.html"
    context_object_name="resultado"
    form_class=ResultadoForm
    success_url=reverse_lazy("anime:listar_resultado") 

class PeleaEdit(generic.UpdateView):
    model=Pelea
    template_name="anime/pelea_Insert.html"
    context_object_name="pelea"
    form_class=PeleaForm
    success_url=reverse_lazy("anime:listar_pelea") 

 #ELIMINACIONES
class DemonioDelete(generic.DeleteView):
    model=Demonio
    template_name="anime/demonio_delete.html"
    context_object_name="obj"
    form_class=DemonioForm
    success_url=reverse_lazy("anime:listar_demonio")

class ParteDelete(generic.DeleteView):
    model=ParteDelCuerpo
    template_name="anime/parte_delete.html"
    context_object_name="parte"
    form_class=ParteForm
    success_url=reverse_lazy("anime:listar_parte")

class CiudadDelete(generic.DeleteView):
    model=Ciudad
    template_name="anime/ciudad_delete.html"
    context_object_name="ciudad"
    form_class=CiudadForm
    success_url=reverse_lazy("anime:listar_ciudad")  

class PersonajeDelete(generic.DeleteView):  
    model=Personaje
    template_name="anime/personaje_delete.html"
    context_object_name="personaje"
    form_class=PersonajeForm
    success_url=reverse_lazy("anime:listar_personaje")    

class ArticuloDelete(generic.DeleteView):  
    model=Articulo
    template_name="anime/articulo_delete.html"
    context_object_name="articulo"
    form_class=ArticuloForm
    success_url=reverse_lazy("anime:listar_articulo")   

class ResultadoPeleaDelete(generic.DeleteView):
    model=ResultadoPelea
    template_name="anime/resultado_pelea_delete.html"
    context_object_name="resultado"
    form_class=ResultadoForm
    success_url=reverse_lazy("anime:listar_resultado") 

class PeleaDelete(generic.DeleteView):
    model=Pelea
    template_name="anime/pelea_delete.html"
    context_object_name="pelea"
    form_class=PeleaForm
    success_url=reverse_lazy("anime:listar_pelea")

def demonio_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    demonios = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Demonios", styles['Heading1'])
    demonios.append(header)
    headings = ('Id', 'Nombre', 'Parte del cuerpo', 'Ciudad')
    if not pk:
        todosdemonios = [(d.id, d.nombre, d.partedelcuerpo, d.ciudad)
                           for d in Demonio.objects.all().order_by('pk')]
    else:
        todosdemonios = [(d.id, d.nombre, d.partedelcuerpo, d.ciudad)
                           for d in Demonio.objects.filter(id=pk)]
    
    t = Table([headings] + todosdemonios)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    demonios.append(t)
    doc.build(demonios)
    response.write(buff.getvalue())
    buff.close()
    return response