# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import JUGADORES
from .models import EQUIPOS
from .models import FOTOS
from .models import CLASIFICACION
from .models import PICHICHI
from .models import ASISTENCIAS
from .models import GOLES_ENCAJADOS
from .models import GOLEADORES_EQUIPOS
from .models import NOTICIAS
from .models import ESCUDOS
from .serializers import JugadorSerializer
from .serializers import EquiposSerializer
from .serializers import FotosSerializer
from .serializers import AsistenciasSerializer
from .serializers import ClasificacionSerializer
from .serializers import PichichiSerializer
from .serializers import Goles_encajadosSerializer
from .serializers import Goleadores_equiposSerializer
from .serializers import Noticias_serializer
from .serializers import EscudosSerializer

# Create your views here.


class JugadorView(viewsets.ModelViewSet):
    search_fields = ['Actualizacion']
    filter_backends = (filters.SearchFilter,)
    serializer_class = JugadorSerializer
    queryset = JUGADORES.objects.all()


class EquipoView(viewsets.ModelViewSet):
    search_fields = ['Actualizacion']
    filter_backends = (filters.SearchFilter,)
    serializer_class = EquiposSerializer
    queryset = EQUIPOS.objects.all()


class Fotoview(viewsets.ModelViewSet):
    serializer_class = FotosSerializer
    queryset = FOTOS.objects.all()


class Clasificacionview(viewsets.ModelViewSet):
    serializer_class = ClasificacionSerializer
    queryset = CLASIFICACION.objects.all()


class Pichichiview(viewsets.ModelViewSet):
    serializer_class = PichichiSerializer
    queryset = PICHICHI.objects.all()


class Asistenciaview(viewsets.ModelViewSet):
    serializer_class = AsistenciasSerializer
    queryset = ASISTENCIAS.objects.all()


class Goles_encajadosview(viewsets.ModelViewSet):
    serializer_class = Goles_encajadosSerializer
    queryset = GOLES_ENCAJADOS.objects.all()


class Goleadores_equiposview(viewsets.ModelViewSet):
    serializer_class = Goleadores_equiposSerializer
    queryset = GOLEADORES_EQUIPOS.objects.all()


class Noticiasview(viewsets.ModelViewSet):
    serializer_class = Noticias_serializer
    queryset = NOTICIAS.objects.all()


class EscudosView(viewsets.ModelViewSet):
    serializer_class = EscudosSerializer
    queryset = ESCUDOS.objects.all()
    
