class DetallePedido(object):

    def __init__(self, codigo_pedido: str = None, codigo_producto: str = None, cantidad: int = None, subtotal: float = None):
        self.__codigo_pedido = codigo_pedido
        self.__codigo_producto = codigo_producto
        self.__cantidad = cantidad
        self.__subtotal = subtotal

    @property
    def codigo_pedido(self):
        return self.__codigo_pedido

    @property
    def codigo_producto(self):
        return self.__codigo_producto

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def subtotal(self):
        return self.__subtotal

    @cantidad.setter
    def cantidad(self, new_value):
        self.__cantidad = new_value

    @subtotal.setter
    def subtotal(self, new_value):
        self.__subtotal = new_value

    def actualizar_datos(self)-> bool:
        """Actualiza los datos del objeto en la db."""
        estado_op = False
        database = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            cursor = database.cursor()
            query = """UPDATE detalle_pedidos SET cantidad = '{}', subtotal = '{}'
            WHERE codigo_pedido = '{}' AND codigo_producto = '{}'""".format(self.__cantidad, self.__subtotal, self.__codigo_pedido, self.codigo_producto)
            cursor.execute(query)
            database.commit()
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op

    @staticmethod
    def obtener_detalle_pedido(codigo_pedido: str, codigo_producto: str):
        """Recibe un codigo_pedido y un codigo_producto como str.
            Devuelve un objeto DetallePedido."""
        detalle_pedido = None
        try:
            database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = """SELECT * FROM detalle_pedidos WHERE codigo_pedido = '{}' AND codigo_producto = '{}'""".format(codigo_pedido, codigo_producto)
            cursor.execute(query)
            detalle_pedido = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
        return DetallePedido(codigo_pedido = detalle_pedido[0], codigo_producto = detalle_pedido[1], cantidad = detalle_pedido[2], subtotal = detalle_pedido[3])


    def calcular_subtotal(self):
        """Calcula el subtotal"""
        subtotal = None
        # Conexión a base de datos
        db = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT cantidad, productos.precio_normal * (1 - productos.descuento)
                        FROM detalle_pedidos JOIN productos  ON detalle_pedidos.codigo_producto = productos.codigo
                        WHERE codigo_pedido = '{}' AND codigo_producto = '{}'""".format(self.__codigo_pedido, self.__codigo_producto)
            #Ejecutar SELECT
            cursor.execute(query)
            #Asignar suma de subtotales a tarifa
            tarifa = cursor.fetchone()
        except Exception as e:
            #Hacer rollback en caso de error
            database.rollback()
            raise e
        finally:
            #Cerrar conexion a db
            db.close()
        print(subtotal)
        self.__subtotal = subtotal
        self.actualizar_datos()
