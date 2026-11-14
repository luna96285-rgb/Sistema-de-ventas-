from django.db import models

# Create your models here.


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Descuentos(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    id_producto_fk = models.ForeignKey('self', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'descuentos'


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido_fk = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido_fk', blank=True, null=True)
    id_productos_fk = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_productos_fk', blank=True, null=True)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Direcciones(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_fk', blank=True, null=True)
    direccion = models.CharField(max_length=200)
    id_municipio_fk = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='id_municipio_fk')
    codigo_postal = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'


class EstadoPedido(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Facturas(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_pedido_fk = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido_fk')
    numero_factura = models.CharField(max_length=40)
    fecha_emision = models.DateField()
    precio_total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'facturas'


class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    codigo_dane = models.CharField(max_length=50)
    municipio = models.CharField(max_length=100)
    id_departamento_fk = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_fk', blank=True, null=True)
    id_direccion_fk = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='id_direccion_fk', blank=True, null=True)
    id_trasportadora_fk = models.ForeignKey('Transportadoras', models.DO_NOTHING, db_column='id_trasportadora_fk', blank=True, null=True)
    fecha_pedido = models.DateField()
    id_estado_fk = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria_fk = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria_fk', blank=True, null=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productos'


class Transportadoras(models.Model):
    id_transportadora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    linea = models.CharField(max_length=300, blank=True, null=True)
    sitio_web = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportadoras'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50)
    telefono = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'usuarios'
