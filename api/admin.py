from django.contrib import admin
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


class ESCUDOSADMIN(admin.ModelAdmin):
    list_display = ('id', 'Equipo', 'Link')


class JUGADORESADMIN(admin.ModelAdmin):
    list_display = ('id', 'jugador', 'edad', 'pais', 'equipos', 'dorsal',
                    'posicion', 'precio', 'actualizacion')


class EQUIPOSADMIN(admin.ModelAdmin):
    list_display = ('id', 'Equipo', 'Jugadores', 'EdadMedia',
                    'ValorTotal', 'ValorMedio', 'Actualizacion')


class FOTOSADMIN(admin.ModelAdmin):
    list_display = ('id', 'Equipo', 'Nombre', 'LinkFoto')


class CLASIFICACIONADMIN(admin.ModelAdmin):
    list_display = ('id', 'Equipo', 'Puntos')


class PICHICHIADMIN(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Goles')


class ASISTENCIASADMIN(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Asistencias')


class GOLESENCAJADOSADMIN(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Goles_encajados')


class GOLEADORESADMIN(admin.ModelAdmin):
    list_display = ('id', 'Equipo', 'Nombre', 'Goles')


class NOTICIASADMIN(admin.ModelAdmin):
    list_display = ('id', 'Titulo', 'Foto', 'Contenido', 'Equipo')


# Register your models here.

admin.site.register(JUGADORES, JUGADORESADMIN)
admin.site.register(ESCUDOS, ESCUDOSADMIN)
admin.site.register(NOTICIAS, NOTICIASADMIN)
admin.site.register(GOLEADORES_EQUIPOS, GOLEADORESADMIN)
admin.site.register(GOLES_ENCAJADOS, GOLESENCAJADOSADMIN)
admin.site.register(PICHICHI, PICHICHIADMIN)
admin.site.register(ASISTENCIAS, ASISTENCIASADMIN)
admin.site.register(CLASIFICACION, CLASIFICACIONADMIN)
admin.site.register(FOTOS, FOTOSADMIN)
admin.site.register(EQUIPOS, EQUIPOSADMIN)


