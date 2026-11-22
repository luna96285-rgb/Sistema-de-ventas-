from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(unique=True, max_length=20)
    id_usuario_fk = models.OneToOneField(
        User,
        models.CASCADE,
        db_column='id_usuario_fk',
        related_name='usuario',
    )

    class Meta:
        managed = True
        db_table = 'usuarios'


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=50)
    municipio = models.CharField(max_length=100)
    id_departamento_fk = models.ForeignKey(
        Departamentos, models.DO_NOTHING,
        db_column='id_departamento_fk', blank=True, null=True,
    )

    class Meta:
        managed = False
        db_table = 'municipio'


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey(
        Usuarios, models.DO_NOTHING,
        db_column='id_usuario_fk', blank=True, null=True,
    )
    direccion = models.CharField(max_length=200)
    id_municipio_fk = models.ForeignKey(
        Municipio, models.DO_NOTHING, db_column='id_municipio_fk',
    )
    codigo_postal = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'
