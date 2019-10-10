from usuario import Usuario
from datetime import datetime
import sqlite3

class Colaborador(object):
    def __init__(self, dni: str = None, nombres: str = None, ape_pat: str = None, ape_mat: str = None,
                 genero: str = None, fecha_nac: datetime = None, fecha_creacion: datetime = None, estado: str = None,
                 email: str = None, password: str = None, reputacion: float = None, cobertura: str = None):

        Usuario.__init__(self, dni, nombres, ape_pat, ape_mat, genero, fecha_nac, fecha_creacion, estado, email, password)
        self.__reputacion = reputacion
        self.__cobertura = cobertura

    @property
    def reputacion(self) -> float:
        return self.__reputacion

    @property
    def cobertura(self) -> str:
        return self.__cobertura

    @reputacion.setter
    def reputacion(self, new_value):
        self.__reputacion = new_value

    @cobertura.setter
    def cobertura(self, new_value):
        self.__cobertura = new_value

    @staticmethod
    def obtener_colaborador(id: str):
        """Recibe un primary key de un colaborador como str. Devuelve un objeto Colaborador."""

        colaborador = None
        try:
            #Conexion a db
            db = sqlite3.connect("linioexp_parcial_lab3.db")
            #Objeto cursor
            cursor = db.cursor()
            query = """SELECT * FROM colaboradores WHERE email = '{}'""".format(id)
            cursor.execute(query)
            colaborador = cursor.fetchone()
        except Exception as e:
            print("Error: {}".format(e))
        finally:
            #cerrar conexión
            database.close()

        return Colaborador(email = colaborador[0], password = colaborador[1], dni = colaborador[2], nombres = colaborador[3],
                       ape_pat = colaborador[4], ape_mat = colaborador[5], genero = colaborador[6], fecha_nac = colaborador[7],
                       fecha_creacion = colaborador[8], estado = colaborador[9], reputacion = colaborador[10], cobertura = colaborador[11])


    def actualizar_datos(self)-> bool:
        """Actualiza los datos del objeto en la db."""
        estado_op = False
        database = sqlite3.connect("linioexp_parcial_lab3.db")
        try:
            cursor = database.cursor()
            query = """UPDATE colaboradores SET password = '{}', documento_identidad = '{}', nombres = '{}', apellido_paterno = '{}',
                        apellido_materno = '{}', genero = '{}', fecha_nacimiento = '{}', estado = '{}', reputacion = '{}', cobertura = '{}'
                        WHERE email = '{}'""".format(self.documento_identidad, self.nombres, self.apellido_paterno,
                        self.apellido_materno, self.genero, self.fecha_nac, self.estado, self.__reputacion, self.__cobertura)
            cursor.execute(query)
            database.commit()
            estado_op = True
        except Exception as e:
            database.rollback()  # RESTAURAR ANTES DE CAMBIOS POR ERROR
            print("Error: {}".format(e))
        finally:
            database.close()  # CERRAR CONEXION CON BASE DE DATOS

        return estado_op
