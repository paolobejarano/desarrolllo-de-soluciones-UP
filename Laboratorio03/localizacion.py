class Localizacion(object):

    def __init__(self, distrito: str = None, provincia: str = None, departamento: str = None):
        self.__distrito = distrito
        self.__provincia = provincia
        self.__departamento = departamento

    @property
    def distrito(self):
        return self.__distrito

    @property
    def provincia(self):
        return self.__provincia

    @property
    def departamento(self):
        return self.__departamento

    @distrito.setter
    def distrito(new_value):
        self.__distrito = new_value

    @provincia.setter
    def provincia(new_value):
        self.__provincia = new_value

    @departamento.setter
    def departamento(new_value):
        self.__departamento = new_value

    def agregar_zona(self):
        pass
