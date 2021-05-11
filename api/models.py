from django.db import models

# Create your models here.


class JUGADORES(models.Model):
    jugador = models.TextField(max_length=120)
    edad = models.IntegerField()
    pais = models.TextField(max_length=120)
    equipos = models.TextField(max_length=120)
    dorsal = models.IntegerField()
    posicion = models.TextField(max_length=120)
    precio = models.FloatField()
    actualizacion = models.TextField(max_length=120)

    def _str_(self):
        return self.jugador


class EQUIPOS(models.Model):
    Equipo = models.TextField(max_length=120)
    Jugadores = models.IntegerField()
    EdadMedia = models.IntegerField()
    ValorTotal = models.FloatField()
    ValorMedio = models.FloatField()
    Actualizacion = models.TextField(max_length=120)

    def _str_(self):
        return self.Equipo


class FOTOS(models.Model):
    Equipo = models.TextField(max_length=120)
    Nombre = models.TextField(max_length=120)
    LinkFoto = models.TextField(max_length=400)

    def _str_(self):
        return self.LinkFoto


class CLASIFICACION(models.Model):
    Equipo = models.TextField(max_length=120)
    Puntos = models.IntegerField()

    def _str_(self):
        return self.Equipo


class PICHICHI(models.Model):
    Nombre = models.TextField(max_length=120)
    Goles = models.IntegerField()

    def _str_(self):
        return self.Nombre


class ASISTENCIAS(models.Model):
    Nombre = models.TextField(max_length=120)
    Asistencias = models.IntegerField()

    def _str_(self):
        return self.Asistencias


class GOLES_ENCAJADOS(models.Model):
    Nombre = models.TextField(max_length=120)
    Goles_encajados = models.IntegerField()

    def _str_(self):
        return self.Goles_encajados


class GOLEADORES_EQUIPOS(models.Model):
    Equipo = models.TextField(max_length=120)
    Nombre = models.TextField(max_length=120)
    Goles = models.IntegerField()

    def _str_(self):
        return self.Nombre


class NOTICIAS(models.Model):
    Titulo = models.TextField(max_length=1000)
    Foto = models.TextField(max_length=1000)
    Contenido = models.TextField(max_length=10000)
    Equipo = models.TextField(max_length=120)

    def _str_(self):
        return self.Titulo
    
class ESCUDOS(models.Model):
    Equipo = models.TextField(max_length=1000)
    Link = models.TextField(max_length=1000)
    
    def _str_(self):
        return self.Equipo
