from django.db import models


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria_fk = models.ForeignKey(
        Categorias, models.DO_NOTHING,
        db_column='id_categoria_fk', blank=True, null=True,
    )
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productos'


class Descuentos(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    # PENDIENTE: verificar en MySQL si id_producto_fk referencia productos.
    # Se conserva 'self' como en los modelos originales para no asumir cambios.
    id_producto_fk = models.ForeignKey(
        'self', models.DO_NOTHING,
        db_column='id_producto_fk', blank=True, null=True,
    )
    porcentaje = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'descuentos'
