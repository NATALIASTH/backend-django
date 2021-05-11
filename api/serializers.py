from rest_framework import serializers
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

class EscudosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESCUDOS
        fields = ('id', 'Equipo', 'Link')
    
class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = JUGADORES
        fields = ('id', 'jugador', 'edad', 'pais', 'equipos', 'dorsal',
                  'posicion', 'precio', 'actualizacion')


class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = EQUIPOS
        fields = ('id', 'Equipo', 'Jugadores', 'EdadMedia',
                  'ValorTotal', 'ValorMedio', 'Actualizacion')


class FotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = FOTOS
        fields = ('id', 'Equipo', 'Nombre', 'LinkFoto')


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLASIFICACION
        fields = ('id', 'Equipo', 'Puntos')


class PichichiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PICHICHI
        fields = ('id', 'Nombre', 'Goles')


class AsistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASISTENCIAS
        fields = ('id', 'Nombre', 'Asistencias')


class Goles_encajadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOLES_ENCAJADOS
        fields = ('id', 'Nombre', 'Goles_encajados')


class Goleadores_equiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = GOLEADORES_EQUIPOS
        fields = ('id', 'Equipo', 'Nombre', 'Goles')


class Noticias_serializer(serializers.ModelSerializer):
    class Meta:
        model = NOTICIAS
        fields = ('id', 'Titulo', 'Foto', 'Contenido', 'Equipo')
