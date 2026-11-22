# Modelos y relaciones — Bella Studio

Este diagrama representa los modelos Django de la rama `rama_martinez` **después de la reorganización**. Se conservaron los nombres de tablas y columnas (`db_table`, `db_column`) existentes. No confirma restricciones SQL que no se hayan inspeccionado directamente en MySQL.

## Distribución de responsabilidades

- **usuarios:** Usuarios, Departamentos, Municipio, Direcciones.
- **catalogo:** Categorias, Productos, Descuentos.
- **ventas:** EstadoPedido, Transportadoras, Pedidos, DetallePedido, Facturas.
- **auth.User (Django):** cuentas y credenciales asociadas a Usuarios.

## Diagrama relacional lógico

```mermaid
erDiagram
    AUTH_USER ||--o| USUARIOS : id_usuario_fk
    DEPARTAMENTOS ||--o{ MUNICIPIO : id_departamento_fk
    USUARIOS ||--o{ DIRECCIONES : id_usuario_fk
    MUNICIPIO ||--o{ DIRECCIONES : id_municipio_fk
    CATEGORIAS ||--o{ PRODUCTOS : id_categoria_fk
    USUARIOS ||--o{ PEDIDOS : id_usuario_fk
    DIRECCIONES ||--o{ PEDIDOS : id_direccion_fk
    TRANSPORTADORAS ||--o{ PEDIDOS : id_trasportadora_fk
    ESTADO_PEDIDO ||--o{ PEDIDOS : id_estado_fk
    PEDIDOS ||--o{ DETALLE_PEDIDO : id_pedido_fk
    PRODUCTOS ||--o{ DETALLE_PEDIDO : id_productos_fk
    PEDIDOS ||--o{ FACTURAS : id_pedido_fk
    DESCUENTOS ||--o{ DESCUENTOS : id_producto_fk_actual

    AUTH_USER {
        int id PK
        string username
        string email
    }
    USUARIOS {
        int id_usuario PK
        string nombre
        string apellido
        string telefono
        int id_usuario_fk FK
    }
    DEPARTAMENTOS {
        int id_departamento PK
        string codigo_dane
        string nombre
    }
    MUNICIPIO {
        int id_municipio PK
        string codigo_dane
        string municipio
        int id_departamento_fk FK
    }
    DIRECCIONES {
        int id_direccion PK
        int id_usuario_fk FK
        int id_municipio_fk FK
        string direccion
    }
    CATEGORIAS {
        int id_categoria PK
        string nombre
    }
    PRODUCTOS {
        int id_producto PK
        int id_categoria_fk FK
        decimal precio
        int stock
    }
    DESCUENTOS {
        int id_descuento PK
        int id_producto_fk FK
        decimal porcentaje
    }
    PEDIDOS {
        int id_pedido PK
        int id_usuario_fk FK
        int id_direccion_fk FK
        int id_trasportadora_fk FK
        int id_estado_fk FK
    }
    ESTADO_PEDIDO {
        int id_estado PK
        string estado
    }
    TRANSPORTADORAS {
        int id_transportadora PK
        string nombre
    }
    DETALLE_PEDIDO {
        int id_detalle PK
        int id_pedido_fk FK
        int id_productos_fk FK
        int cantidad
        decimal precio_unitario
    }
    FACTURAS {
        int id_factura PK
        int id_pedido_fk FK
        string numero_factura
    }
```

> **Pendiente crítico de verificación:** el modelo original `Descuentos.id_producto_fk` apunta a `'self'` (la tabla descuentos), aunque por su nombre parece apuntar a `productos`. **No se modificó** esta relación sin conocer la clave foránea real de MySQL. La flecha de descuentos en este gráfico refleja el **código actual**, no necesariamente el diseño deseado.

## Estado de migraciones y precauciones

Las migraciones `0001_initial.py` antiguas conservan declaraciones de modelos duplicados y algunas definiciones anteriores. Esta reorganización es una **refactorización de las clases Python**, no una migración física de la base de datos.

**Antes de generar o aplicar nuevas migraciones:** revisar el plan de cambios y el estado de migraciones; no ejecutar `migrate` a ciegas. La tabla `usuarios` ya está en uso y no debe recrearse.

## Pruebas recomendadas al bajar la rama

1. `python manage.py check`
2. `python manage.py showmigrations`
3. Revisar `python manage.py makemigrations --dry-run --verbosity 2` sin aplicar cambios.
4. Comprobar las consultas ORM y relaciones, preferiblemente en una base de datos de prueba.

**No se cambió ninguna estructura SQL ni se aplicó una migración.**
