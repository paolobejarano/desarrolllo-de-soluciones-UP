from datetime import datetime
import sqlite3
from colaborador import Colaborador
from localizacion import Localizacion
from cliente import Cliente

class Pedido(object):

    def __init__(self, codigo: str = None, cliente = Cliente(), fechaCreacion: datetime = None, estado: str = None, fechaEntrega: datetime = None, direccionEntrega: str = None, repartidor = Colaborador(), ubicacion = Localizacion(), tarifa: float = None):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__fechaCreacion = fechaCreacion
        self.__estado = estado
        self.__fechaEntrega = fechaEntrega
        self.__direccionEntrega = direccionEntrega
        self.__repartidor = repartidor
        self.__ubicacion = ubicacion
        self.__tarifa = tarifa

    @property
    def codigo(self):
        return self.__codigo

    @property
    def fechaCreacion(self):
        return self.__fechaCreacion

    @property
    def estado(self):
        return self.__estado

    @property
    def fechaEntrega(self):
        return self.__fechaEntrega

    @property
    def direccionEntrega(self):
        return self.__direccionEntrega

    @property
    def repartidor(self):
        return self.__repartidor

    @property
    def ubicacion(self):
        return self.__ubicacion

    @codigo.setter
    def codigo(self, new_value):
        self.__codigo = new_value

    @fechaCreacion.setter
    def fechaCreacion(self, new_value):
        self.__fechaCreacion = new_value

    @estado.setter
    def estado(self, new_value):
        self.__estado = new_value

    @fechaEntrega.setter
    def fechaEntrega(self, new_value):
        self.__fechaEntrega = new_value

    @direccionEntrega.setter
    def direccionEntrega(self, new_value):
        self.__direccionEntrega = new_value

    @repartidor.setter
    def repartidor(self, new_value):
        self.__repartidor = new_value

    @ubicacion.setter
    def ubicacion(self, new_value):
        self.__ubicacion = new_value

    def generar_codigo(self) -> str:
        count = 0
        #Conexión a base de datos
        db = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            #Objeto cursor
            cursor = db.cursor()
            #Contar el numero de pedidos en la db
            query = "SELECT COUNT(*) FROM pedidos"
            cursor.execute(query)
            count = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #Cerrar conexión a db
            database.close()

        return "Pedido" + "0"*(4 - len(str(count[0] + 1))) + str(count[0] + 1)

    def actualizar_datos(self)-> bool:
        """Actualiza los datos del objeto en la db."""
        estado_op = False
        database = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            cursor = database.cursor()
            query = """UPDATE pedidos SET codigo_cliente = '{}', codigo_colaborador = '{}', estado = '{}', fecha_entrega = '{}',
                        direccion_entrega = '{}', tarifa = '{}', codigo_zona = '{}' WHERE codigo = '{}'""".format(self.__cliente.email, self.__repartidor.email,
                        self.__estado, self.__fecha_entrega, self.__direccionEntrega, self.__tarifa, self.__ubicacion.codigo_zona, self.__codigo)
            cursor.execute(query)
            database.commit()
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op

    def calcular_tarifa(self):
        """Calcula el precio total, lo muestra y lo actualiza en la db."""
        tarifa = None
        # Conexión a base de datos
        db = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT SUM(detalle_pedidos.subtotal) FROM detalle_pedidos WHERE codigo_pedido = '{}'""".format(self.__codigo)
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
        print(tarifa)
        self.__tarifa = tarifa
        self.actualizar_datos()

    def listar_pedidos_estado(self, estado: str):
        """Recibe un str que es el estado. Lista todos los pedidos en la db que coincidan con el estado."""
        pedidos = None
        try:
            database = sqlite3.connect("linioexp_parcial_lab3.db")  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = """SELECT * FROM pedidos WHERE estado = '{}'""".format(estado)
            cursor.execute(query)
            count = cursor.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

    def asignar_repartidor(self, repartidor = Colaborador()):
        """Recibe un objeto repartidor. Asigna el repartidor al pedido en la db."""
        id_repartidor = repartidor.email
        #Conexión a base de datos
        db = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            #Objeto cursor
            cursor = db.cursor()
            query = """UPDATE pedidos SET codigo_colaborador = '{}'""".format(id_repartidor)
            #Ejecutar Update
            cursor.execute(query)
            #Confirmar cambios
            database.commit()
        except Exception as e:
            #Hacer rollback en caso de error
            database.rollback()
            raise e
        finally:
            #Cerrar conexion a db
            db.close()
