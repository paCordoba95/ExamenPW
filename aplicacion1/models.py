from django.db import models
from django.contrib import admin
# Create your models here.

class Nav(models.Model):
       id_nav = models.AutoField(db_column= "idNav",primary_key=True)
       nombre_nav = models.CharField(max_length=20, blank=False, null=False)
       enlace_nav = models.CharField(max_length=300, blank=False, null=False)

       def  __str__(self):
              return self.nombre_nav


