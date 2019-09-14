import sqlite3
con = sqlite3.connect('Linioexp_parcial.db')
cursor = con.cursor()

def drop_tables():
    """Borra todas las tablas de la db"""
    cursor.execute("DROP TABLE cliente")
    cursor.execute("DROP TABLE pedido")
    cursor.execute("DROP TABLE producto")
    cursor.execute("DROP TABLE linea_pedido")

cursor.execute("""
  CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombres TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    documento_identidad TEXT NOT NULL,
    email TEXT NOT NULL,
    fecha_registro DATETIME)""")

#Comando para realizar cambios
con.commit()

#Creacion de tabla pedido
cursor.execute("""
  CREATE TABLE IF NOT EXISTS pedido (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    fecha_registro DATETIME NOT NULL,
    fecha_entrega DATETIME NOT NULL,
    estado VARCHAR(30) NOT NULL,
    precio_total DECIMAL(8, 2) NOT NULL,
    cantidad_total INTEGER NOT NULL,
    direccion VARCHAR(150) NOT NULL,
    distrito VARCHAR(150) NOT NULL,
    provincia VARCHAR(150) NOT NULL,
    departamento VARCHAR(150) NOT NULL,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente))""")

#Comando para realizar cambios
con.commit()

#Creacion de tabla producto
cursor.execute("""
  CREATE TABLE IF NOT EXISTS producto (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(250) NOT NULL,
    descripcion VARCHAR(1000) NOT NULL,
    marca VARCHAR(250) NOT NULL,
    precio DECIMAL(8,2) NOT NULL,
    stock INTEGER NOT NULL)""")

#Comando para realizar cambios
con.commit()

#Creacion de tabal linea_pedido
cursor.execute("""
  CREATE TABLE IF NOT EXISTS linea_pedido (
    id_linea_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_producto INTEGER NOT NULL,
    id_pedido INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    valor_unitario DECIMAL(8,2),
    subtotal DECIMAL(10,2),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto),
    FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido))""")

#Consultas SQL
print("Número de clientes registrados")
for row in cursor.execute("""SELECT COUNT(*) FROM cliente"""):
    print(row)

print("Clientes que pidieron con destino al Callao")
for row in cursor.execute("""SELECT cliente.* FROM pedido, cliente WHERE pedido.id_cliente = cliente.id_cliente AND pedido.distrito = 'CALLAO'"""):
    print(row)

print("Clientes que compraron el 2018-12-24")
for row in cursor.execute("""SELECT cliente.nombres, cliente.apellidos, pedido.fecha_registro FROM cliente, pedido WHERE cliente.id_cliente = pedido.id_cliente AND pedido.fecha_registro = '24-12-2018 01:15:20 pm'"""):
    print(row)

print("¿Cuál es el cliente que realizó el mayor gasto en comprar productos en LinioExp? (Puedes encontrar más de un cliente con el mayor gasto)")
#La siguiente sentencia me permite obtener el mayor número de pedidos por cliente
for row in cursor.execute('SELECT SUM(precio_total) FROM pedido GROUP BY pedido.id_cliente ORDER BY SUM(precio_total) DESC LIMIT 1'):
    print(row)
#Luego busco qué clientes coincicen con este número por si hay más de uno
for row in cursor.execute('SELECT cliente.nombres, cliente.apellidos, SUM(precio_total) FROM pedido INNER JOIN cliente ON pedido.id_cliente = cliente.id_cliente GROUP BY pedido.id_cliente HAVING SUM(precio_total) = (SELECT SUM(precio_total) FROM pedido GROUP BY pedido.id_cliente ORDER BY SUM(precio_total) DESC LIMIT 1);'):
    print(row)

print("¿Cuál es el producto más vendido? (Pueden haber uno o más productos más vendidos)")
#La siguiente sentencia permite obtener el mayor número de pedidos por cada producto
for row in cursor.execute('SELECT SUM(cantidad) FROM linea_pedido GROUP BY linea_pedido.id_producto ORDER BY SUM(cantidad) DESC LIMIT 1;'):
    print(row)
#Luego busco qué productos coinciden con este número por si hay más de uno
for row in cursor.execute('SELECT producto.nombre, SUM(cantidad) FROM linea_pedido INNER JOIN producto ON linea_pedido.id_producto = producto.id_producto GROUP BY linea_pedido.id_producto HAVING SUM(cantidad) = (SELECT SUM(cantidad) FROM linea_pedido GROUP BY linea_pedido.id_producto ORDER BY SUM(cantidad) DESC LIMIT 1)'):
    print(row)
