from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import (UpdateView)

from vhsApp.models import Cassette, Membresia, Solicitar



def about(request):

    return render(
        request=request,
        template_name='vhsApp/about.html',
    )

def inicio(request):

    return render(
        request=request,
        template_name='vhsApp/inicio.html',
    )

@login_required
def listar_cassettes(request):

    contexto = {
        'cassettes': Cassette.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_cassettes.html',
        context=contexto,
    )

@login_required
def listar_membresias(request):

    contexto = {
        'membresias': Membresia.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_membresias.html',
        context=contexto,
    )

@login_required
def listar_solicitudes(request):

    contexto = {
        'solicitud': Solicitar.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_solicitudes.html',
        context=contexto,
    )

def buscar_cassettes(request):

      if  request.method == "POST":

            data = request.POST 
            cassettes = Cassette.objects.filter(
                Q(nombre__contains=data['busqueda']) |
                Q(genero__contains=data['busqueda'])
            )

            contexto = {'cassettes' : cassettes}

            return render(
                request=request,
                template_name='vhsApp/listar_cassettes.html',
                context=contexto,
            )

      else:
        
        respuesta = "No hay datos"

        return render(
            request=request,
            template_name='vhsApp/listar_cassettes.html',
            respuesta=respuesta,
            )

@login_required
def crear_cassettes(request):

    if request.method == "POST":

        formulario = CassetteFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            cassette = Cassette(
                          nombre=data['nombre'],
                          genero=data['genero'],
                          año=data['año'],
                          autor=data['autor'],
                          descripcion=data['descripcion']
                         )

            cassette.save()
            url_exitosa = reverse('listar_cassettes')
            return redirect(url_exitosa)

    else:
        formulario = CassetteFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_cassettes.html',
        context={'formulario': formulario},
    )

def crear_solicitudes(request):

    if request.method == "POST":

        formulario = SolicitudFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            solicitud = Solicitar(
                                  solicitud=data['solicitud'],
                                  fecha=data['fecha']
                                 )

            solicitud.save()
            url_exitosa = reverse('listar_solicitudes')
            return redirect(url_exitosa)

    else:
        formulario = SolicitudFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_solicitudes.html',
        context={'formulario': formulario},
    )

def registro(request):

    if request.method == "POST":

        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)

    else:

        formulario = UserRegisterForm()

    return render(
                  request=request,
                  template_name='vhsApp/registro.html',
                  context={'form': formulario},
                 )

def login_request(request):

    next_url = request.GET.get('next')

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario,
                                password=password
                               )

            if user:
                login(request=request, user=user)

                if next_url:
                    return redirect(next_url)

                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)

    else:

        form = AuthenticationForm()

    return render(
                  request=request,
                  template_name='vhsApp/login.html',
                  context={'form': form},
                 )


class RequestLogoutView(LogoutView):

    template_name = 'vhsApp/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'vhsApp/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def agregar_avatar(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)

    else:

        formulario = AvatarFormulario()

    return render(
                  request=request,
                  template_name='vhsApp/formulario_avatar.html',
                  context={'form': formulario},
                 )
