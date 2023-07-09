class Libro:
    def __init__(self, titulo, cantidad, autor, tipo, codigo):
        self._titulo = titulo
        self._cantidad = cantidad
        self._autor = autor
        self._tipo = tipo
        self._codigo = codigo

    def __init_subclass__(self, **kwargs):
        self._titulo = ""
        self._cantidad = ""
        self._autor = ""
        self._tipo = ""
        self._codigo = ""

    #metodos obtener datos
    def getTitulo(self):
        return self._titulo

    def getCantidad(self):
        return self._cantidad

    def getAutor(self):
        return self._autor

    def getTipo(self):
        return self._tipo

    def getCodigo(self):
        return self._codigo

    #metodos crear
    def setTitulo(self, titulo):
        self._titulo = titulo

    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def setAutor(self, autor):
        self._autor = autor

    def setTipo(self, tipo):
        self._tipo = tipo

    def setCodigo(self, codigo):
        self._codigo = codigo


    def toString(self):
        return f"""
Titulo: {self._titulo}
Cantidad: {self._cantidad}
Autor: {self._autor}
Tipo: {self._tipo}
codigo: {self._codigo}
        """


