import sqlite3


class Producto(object):

    def __init__(self, nombre: str, descripcion: str, precio: float, descuento: float):
        self.__codigo = None
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__descuento = descuento
        self.__precio_desc = self.precio_venta
        self.__estado = "P"

    def agregar_producto(self) -> bool:
        pass

    def actualizar_datos(self) -> bool:
        pass

    @property
    def precio_venta(self) -> float:
        return self.__precio - (self.__precio * self.__descuento)

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, new_value):
        self.__precio = new_value

    def generar_codigo(self) -> str:
        count = 0
        database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            SELECT COUNT(*) FROM productos'''
            cursor.execute(query)
            count = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return "PROD" + "0"*(4 - len(str(count[0] + 1))) + str(count[0] + 1)

    def __str__(self) -> str:
        return "{}-> nombre= {}, precio= {}, estado= {} ".format(self.__class__.__name__,
                                                              self.__nombre, self.__precio,
                                                              self.__estado)

