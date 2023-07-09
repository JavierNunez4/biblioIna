class Prestamos:
    def __init__(self, rutCliente, estado, fentrega, fdevolucion, titulo):
        self._rutCliente = rutCliente
        self._estado = estado
        self._fentrega = fentrega
        self._fdevolucion = fdevolucion
        self._titulo = titulo
        
    
    def __init__(self):
        self._rutCliente = ""
        self._estado = ""
        self._fentrega = ""
        self._fdevolucion = ""
        self._titulo = ""



    #metodos mostrar datos
    def getRutCliente(self):
        return self._rutCliente
    
    def getEstado(self):
        return self._estado
    
    def getFechaEntrega(self):
        return self._fentrega
    
    def getFechaDev(self):
        return self._fdevolucion
    
    def getTitulo(self):
        return self._titulo
    
    #metodos agregar

    def setRutCliente(self, rutCliente):
        self._rutCliente = rutCliente
    
    def setEstado(self, estado):
        self._estado = estado

    def setFechaEntrega(self, fentrega):
        self._fentrega = fentrega
    
    def setFechaDev(self, fdevolucion):
        self._fdevolucion = fdevolucion

    def setTitulo(self, titulo):
        self._titulo = titulo

    def toString(self):
        return f"""
Rut Cliente: {self._rutCliente}
Estado del libro: {self._estado}
Fecha de entrega: {self._fentrega}
Fecha de devolucion: {self._fdevolucion}
Titulo del libro: {self._titulo}
        """

    