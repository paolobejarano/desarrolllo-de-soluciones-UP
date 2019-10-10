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
        estado_op = False
        database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            print(self.generar_codigo())
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = """INSERT INTO productos(codigo, nombre, descripcion, precio_venta, precio_normal,
                    estado, descuento) VALUES ('{}', '{}', '{}', {}, {},'{}',{})""".format(self.generar_codigo(),
                    self.__nombre, self.__descripcion, self.precio_venta, self.__precio,self.__estado, self.__descuento)
            cursor.execute(query)
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op

    def actualizar_datos(self) -> bool:
        estado_ope: bool = False
        database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS

        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = '''
            UPDATE productos
            SET descripcion = '{}', precio_normal = {}, estado = '{}',  descuento = {}, precio_venta = {}
            WHERE codigo = '{}'
            '''.format(self.__descripcion, self.__precio, self.__estado, self.__descuento,
                       self.precio_venta, self.__codigo)
            cursor.execute(query)  # EJECUTA LA OPERACION
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado_ope = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            raise e
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_ope

    @property
    def precio_venta(self) -> float:
        return self.__precio - (self.__precio * self.__descuento)

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @property
    def precio(self) -> float:
        return self.__precio

    @property
    def descuento(self) -> float:
        return self.__descuento

    @property
    def estado(self) -> str:
        return self.__estado

    @descripcion.setter
    def descripcion(self, new_value):
        self.__descripcion = new_value

    @precio.setter
    def precio(self, new_value):
        self.__precio = new_value

    @descuento.setter
    def descuento(self, new_value):
        self.__descuento = new_value

    @estado.setter
    def estado(self, new_value):
        self.__estado = new_value

    def generar_codigo(self) -> str:
        count = 0
        database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS
        try:
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = "SELECT COUNT(*) FROM productos;"
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

