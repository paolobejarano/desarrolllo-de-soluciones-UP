from usuario import Usuario
from datetime import datetime
import sqlite3

class Cliente(Usuario):

    LISTA_ESTADO = {"NUEVO":"N", "PENDIENTE": "P", "VALIDADO": "V"}

    def __init__(self, dni: str = None, nombres: str = None, ape_pat: str = None, ape_mat: str = None,
                 genero: str = None, fecha_nac: datetime = None, fecha_creacion: datetime = None,
                 estado: str = None, email: str = None, password: str = None, preferencias: list = None):
        self.referencias = preferencias
        self.email = email
        self.password = password
        self.dni = dni
        self.nombres = nombres
        self.apellido_paterno = ape_pat
        self.apellido_materno = ape_mat
        self.genero = genero
        self.fecha_nacimiento = fecha_nac
        fecha_creacion = datetime.now()
        self.fecha_creacion = fecha_creacion
        self.estado = estado

    def crear_cuenta(self)-> bool:
        estado = False
        try:
            database = sqlite3.connect("linioexp_parcial_lab3.db", timeout=10)  # ABRIR CONEXION CON BASE DE DATOS
            cursor = database.cursor()  # OBTENER OBJETO CURSOR
            query = "INSERT INTO clientes (email, password, estado, fecha_creacion) VALUES ('" # DEFINICION DE OPERACION
            query += str(self.email)
            query += "', '"
            query += str(self.password)
            query += "', 'Nuevo', '"
            query += str(datetime.now())
            query += "')"
            cursor.execute(query)  # EJECUTA LA OPERACION
            database.commit()  # CONFIRMAR CAMBIOS QUERY
            estado = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            raise e
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS
        return estado

    def actualizar_datos(self)-> bool:
        pass

    def obtener_usuario(id: str):
        usuario = None

        return Cliente(email=usuario[0], password=usuario[1], dni=usuario[2], nombres=usuario[3],
                       ape_pat=usuario[4], ape_mat=usuario[5], genero=usuario[6], fecha_nac=usuario[7],
                       fecha_creacion=usuario[8], estado=usuario[9], preferencias=usuario[10])

    def __str__(self):
        return "{}-> email= '{}', estado= '{}', nombre= '{} {} {}'.".format(self.__class__.__name__, self.email,
                                                                            self.estado, self.nombres,
                                                                            self.apellido_paterno,
                                                                            self.apellido_materno)
