class Persona:
    __n: None
    __a: None
    __e: None
    __o: None

    def __init__(self, p1, p2, p3, p4):
        self._set_nombre(p1)
        self._set_apellidoso(p2)
        self._set_edad(p3)
        self._set_oficio(p4)

    def get_nombre(self):
        return self.__n

    def get_apellidos(self):
        return self.__a

    def get_edad(self):
        return self.__e

    def get_oficio(self):
        return self.__o

    def set_nombre(self, n1):
        if '-' in n1 or '_' in n1:
            raise Exception("Los caracteres - o _ no son válidos")
        self.__n = n1

    def set_apellidos(self, a1):
        if '@' in a1 or '&' in a1:
            raise Exception("Los caracteres - o _ no son válidos")
        self.__a = a1

    def set_edad(self, e1):
        if 0 > e1 > 100:
            raise Exception("Edad no posible")
        self.__e = e1

    def set_oficio(self, o1):
        if o1 not in ["Agricultura", "Ganaderia", "Industria", "Turismo", "Servicios"]:
            raise Exception("El oficio no existe")
        self.__o = o1

    def trabajar(self):
        self.set_edad(self.get_edad()+1)
        print("Has aumentado tus habilidades y conocimiento durante este año de trabajo")

