from django.urls import path

from vhsApp import views


urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path('cassettes/', views.listar_cassettes, name="listar_cassettes"),
    path('membresias/', views.listar_membresias, name="listar_membresias"),
    path('solicitudes/', views.listar_solicitudes, name="listar_solicitudes"),
    path('buscar_cassettes/', views.buscar_cassettes, name="buscar_cassettes"),
    path('crear_cassettes/', views.crear_cassettes, name="crear_cassettes"),
    path('crear_solicitudes/', views.crear_solicitudes, name="crear_solicitudes"),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_request, name="login"),
    path('logout/', views.RequestLogoutView.as_view(), name='logout'),
    path('editar-perfil/', views.ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', views.agregar_avatar, name="agregar_avatar"),

]
