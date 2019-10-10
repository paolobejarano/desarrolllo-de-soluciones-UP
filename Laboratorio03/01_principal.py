from producto import Producto
from cliente import Cliente

'''
cliente = Cliente.obtener_usuario("luis.medina.delgado@hotmail.com")
cliente.estado = "Z"
cliente.actualizar_datos()
print(cliente)

# Crear cuenta
cliente_new = Cliente(email="mauroleonpayano@gmail.com", password="demo")
print(cliente_new.crear_cuenta())
'''

producto = Producto("demo", "demo", 17.3, 0.1)
producto.estado = "P"
producto.actualizar_datos()
print(producto.agregar_producto())
