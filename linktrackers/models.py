from django.db import models
from django.conf import settings


# Create your models here.
# En esta clase se definen las tablas en la DB con sus atributos
# tener en cuenta los tipos de datos y la forma en la que se declaran
# tener en cuidado con las constrains

# table links
class link(models.Model):
    link_description = models.TextField(primary_key=True,serialize=True)
    link_url = models.TextField(unique=True)

    class Meta:
        db_table = "links"


class Publicacion(models.Model):
    idPubli = models.AutoField(primary_key=True)
    contenidoPubli = models.TextField(max_length=300)
    numeroLikesPubli = models.IntegerField(max_length=99)
    fechaPubli = models.CharField(max_length=20)
    publicadorPubli = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        db_table = "publicacion"
