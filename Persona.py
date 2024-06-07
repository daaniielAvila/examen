"""
Creamos la clase Persona con sus respectivos parametros privados
"""
class Persona:
    __nombre: None
    __apellidos: None
    __edad: None
    __oficio: None

    def __init__(self, nombre, apellidos, edad, oficio):
        self._set_nombre(nombre)
        self._set_apellidoso(apellidos)
        self._set_edad(edad)
        self._set_oficio(oficio)
        """
        Hacemos todos los getters 
        """       

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_edad(self):
        return self.__edad

    def get_oficio(self):
        return self.__oficio
    """
    Hacemos las comprobaciones de cada parametro en los setters
    """
    def set_nombre(self, nombre):
        if '-' in nombre or '_' in nombre:
            raise Exception("Los caracteres - o _ no son válidos")
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        if '@' in apellidos or '&' in apellidos:
            raise Exception("Los caracteres - o _ no son válidos")
        self.__apellidos = apellidos

    def set_edad(self, edad):
        if 0 > edad > 100:
            raise Exception("Edad no posible")
        self.__edad = edad

    def set_oficio(self, oficio):
        if oficio not in ["Agricultura", "Ganaderia", "Industria", "Turismo", "Servicios"]:
            raise Exception("El oficio no existe")
        self.__oficio = oficio

    def trabajar(self):
        self.set_edad(self.get_edad()+1)
        print("Has aumentado tus habilidades y conocimiento durante este año de trabajo")


