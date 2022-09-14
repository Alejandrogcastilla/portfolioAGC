from django.shortcuts import render
from .models import Mensajes, Visitas
from .form import MessageForm


def inicio(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = Mensajes.objects.create(nombre=form.cleaned_data['nombre'],
                                                  email=form.cleaned_data['email'],
                                                  mensaje=form.cleaned_data['mensaje'], )
            new_message.save()

    new_visita = Visitas.objects.create(peticion=request)
    new_visita.save()

    context = {'form': MessageForm}
    return render(request, 'html/index.html', context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
