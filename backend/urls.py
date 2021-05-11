"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Jugadores', views.JugadorView, 'jugadores')
router.register(r'Equipos', views.EquipoView, 'equipos')
router.register(r'Fotos', views.Fotoview, 'fotos')
router.register(r'Clasificacion', views.Clasificacionview, 'Clasificacion')
router.register(r'Pichichi', views.Pichichiview, 'Pichichi')
router.register(r'Asistencias', views.Asistenciaview, 'Asistencias')
router.register(r'Goles_encajados', views.Goles_encajadosview, 'Goles_encajados')
router.register(r'Goleadores_equipos', views.Goleadores_equiposview, 'Goleadores_equipos')
router.register(r'Noticias',views.Noticiasview,'Noticias')
router.register(r'Escudos',views.EscudosView,'Escudos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]
