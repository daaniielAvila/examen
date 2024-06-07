"""
Creamos la clase Persona con sus respectivos parametros privados
"""
class Persona:
    __nombre: None
    __apellidos: None
    __edad: None
    __oficio: None
    __color_pelo : None

<<<<<<< HEAD
    def __init__(self, nombre, apellidos, edad, oficio):
        self._set_nombre(nombre)
        self._set_apellidoso(apellidos)
        self._set_edad(edad)
        self._set_oficio(oficio)
        """
        Hacemos todos los getters 
        """       
=======
    def __init__(self, nombre, apellidos, edad, oficio, color_pelo):
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_edad(edad)
        self.set_oficio(oficio)
        self.set_color_pelo(color_pelo)
>>>>>>> rama1

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_edad(self):
        return self.__edad

    def get_oficio(self):
        return self.__oficio
<<<<<<< HEAD
    """
    Hacemos las comprobaciones de cada parametro en los setters
    """
=======
    
    def get_color_pelo(self):
        return self.__color_pelo

>>>>>>> rama1
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

    def set_color_pelo(self, color_pelo):
        if color_pelo not in ["Rubio", "Castaño", "Moreno"]:
            raise Exception("Color de pelo no valido")
        self.__color_pelo = color_pelo

    def trabajar(self):
        self.set_edad(self.get_edad()+1)
        print("Has aumentado tus habilidades y conocimiento durante este año de trabajo")


