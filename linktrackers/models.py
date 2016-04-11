from django.db import models


# Create your models here.
# En esta clase se definen las tablas en la DB con sus atributos
# tener en cuenta los tipos de datos y la forma en la que se declaran
# tener en cuidado con las constrains

class link(models.model):
    link_description = models.CharField(max_length=200).db_column
    link_url = models.CharField(max_length=200).primary_key.db_column
