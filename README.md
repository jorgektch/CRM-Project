# CRM-Project
Proyecto de CRM

## Primer avance (Base de datos SQLite)
Diseño y construcción de bases de datos (tablas, relaciones e inserción primaria). Tablas:
- Categoría: Categoría de productos, incluye descripción.
- Cita: Cita entre un trabajador y un cliente, fechada. Puede tener asociados varios productos.
- CitaProducto: Productos a ser considerados en una cita.
- Cliente: Cliente o prospecto de cliente. Se puede agregar un categoría, para conmvertirlo de lead a cliente.
- Motivo: Motivo de una cita, incluye descripción.
- Producto: Producto, incluye imágenes (01 por producto).
- Trabajador: Trabajador de la empresa. Se puede agregar categoría de trabajadores.
- Venta: Venta realizada por un trabajador para un cliente, está fechada.
- Ventaproducto: Porductos asociados una determinada venta.
