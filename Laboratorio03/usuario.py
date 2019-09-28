from datetime import datetime
import sqlite3


class Usuario(object):

    def __init__(self, dni: str = None, nombres: str = None, ape_pat: str = None, ape_mat: str = None,
                 genero: str = None, fecha_nac: datetime = None, fecha_creacion: datetime = None,
                 estado: str = None, email: str = None, password: str = None):
        self.__documento_identidad = dni
        self.__nombres = nombres
        self.__apellido_paterno = ape_pat
        self.__apellido_materno = ape_mat
        self.__genero = genero
        self.__fecha_nac = fecha_nac
        self.__fecha_crea = fecha_creacion
        self.__estado = estado
        self.__email = email
        self.__password = password

    @property
    def estado(self):
        return self.__estado



    @estado.setter
    def estado(self, new_estado: str):
        self.__estado = new_estado
