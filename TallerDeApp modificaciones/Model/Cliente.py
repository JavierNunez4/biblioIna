class Cliente:
    def __init__(self, nombre, apellido, contacto, direccion, ocupacion, rut):
        self._nombre = nombre
        self._apellido = apellido
        self._contacto = contacto
        self._direccion = direccion
        self._ocupacion = ocupacion
        self._rut = rut

    def __init_subclass__(self, **kwargs):
        self._nombre = ""
        self._apellido = ""
        self._contacto = ""
        self._direccion = ""
        self._ocupacion = ""
        self._rut = ""
    
    #metodos para obtener 
    def getNombre(self):
        return self._nombre

    def getApellido(self):
        return self._apellido
    
    def getContacto(self):
        return self._contacto
    
    def getDireccion(self):
        return self._direccion
    
    def getOcupacion(self):
        return self._ocupacion
    
    def getRut(self):
        return self._rut
    

    #Metodos para ingresar
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setApellido(self, apellido):
        self._apellido = apellido

    def setContacto(self,  contacto):
        self._contacto = contacto 

    def setDireccion(self, direccion):
        self._direccion = direccion 

    def setOcupacion(self, ocupacion):
        self._ocupacion = ocupacion 

    def setRut(self, rut):
        self._rut = rut

    def toString(self):
        return f""" 
Nombre: {self._nombre}
Apellido: {self._apellido}
Contacto: {self._contacto}
Direccion: {self._direccion}
Ocupacion: {self._ocupacion}
Rut: {self._rut}
        """