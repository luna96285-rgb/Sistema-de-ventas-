from django.db import models


class EstadoPedido(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Transportadoras(models.Model):
    id_transportadora = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    linea = models.CharField(max_length=300, blank=True, null=True)
    sitio_web = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transportadoras'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey(
        'usuarios.Usuarios', models.DO_NOTHING,
        db_column='id_usuario_fk', blank=True, null=True,
    )
    id_direccion_fk = models.ForeignKey(
        'usuarios.Direcciones', models.DO_NOTHING,
        db_column='id_direccion_fk', blank=True, null=True,
    )
    id_trasportadora_fk = models.ForeignKey(
        Transportadoras, models.DO_NOTHING,
        db_column='id_trasportadora_fk', blank=True, null=True,
    )
    fecha_pedido = models.DateField()
    id_estado_fk = models.ForeignKey(
        EstadoPedido, models.DO_NOTHING,
        db_column='id_estado_fk', blank=True, null=True,
    )

    class Meta:
        managed = False
        db_table = 'pedidos'


class DetallePedido(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido_fk = models.ForeignKey(
        Pedidos, models.DO_NOTHING,
        db_column='id_pedido_fk', blank=True, null=True,
    )
    id_productos_fk = models.ForeignKey(
        'catalogo.Productos', models.DO_NOTHING,
        db_column='id_productos_fk', blank=True, null=True,
    )
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class Facturas(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_pedido_fk = models.ForeignKey(
        Pedidos, models.DO_NOTHING, db_column='id_pedido_fk',
    )
    numero_factura = models.CharField(max_length=40)
    fecha_emision = models.DateField()
    precio_total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'facturas'
