class Categoria():

    def __init__(self, codigo: str = codigo, nombre: str, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.productos = []

    def __str__(self):
        return "codigo: " + self.codigo + ", nombre: " + self.nombre

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)
