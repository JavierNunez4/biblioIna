from Controller.Clientecontroller import *
from Controller.librocontroller import *
from Controller.prestamocontroller import *


def rut_cliente():
    rut = input("Ingrese el Rut del usuario: ")
    return buscar_por_rut(rut)


# Funciones para el cliente
def lista_clientes():
    lista = listar_clientes()
    for user in lista:
        print(user.toString())
    input("Presione ENTER para Volver al menu principal...")


def usuario_nuevo():
    name = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    contact = input("Ingrese el contacto: ")
    direc = input("Ingrese la dirección: ")
    cargo = input("Ingrese la ocupación: ")
    rut = input("Ingrese el Rut: ")
    user = Cliente(name, apellido, contact, direc, cargo, rut)
    agregar_cliente(user)


def eliminar_user():
    rut = input("Ingrese el Rut del Usuario que desea eliminar: ")
    eliminar_cliente(rut)


def menuClientes():
    print("""
Menu Estudiantes y Docentes:
1.- Mostrar los Estudiantes/Docentes
2.- Agregar un Estudiante/Docente
3.- Editar un Estudiante/Docente
4.- Eliminar un Estudiante/Docente  
        """)
    user_select = input("Ingrese su opcion (1, 2, 3 o 4): ")
    if user_select == "1":
        seleccion = input('Ingrese "1" si desea ver todos los usuarios o "2" si desea buscar por rut: ')
        if seleccion == "1":
            return lista_clientes()

        elif seleccion == "2":
            rut = input("Ingrese el rut del Estudiante/Docente: ")
            buscar_por_rut(rut)
            return input("Enter para continuar")

        else:
            input("Opcion invalida... Enter para continuar")

    elif user_select == "2":
        return usuario_nuevo()

    elif user_select == "3":
        rut = input("Ingrese el rut del Estudiante/Docente: ")
        return editar_cliente(rut)

    elif user_select == "4":
        return eliminar_user()

    else:
        input("Recuerde que debe ingresar una opcion valida...")



# funciones para los préstamos
def mostrarPrestamos():
    lista_prestamos = mostrar_prestamos()
    print("\nLista de prestamos:")
    for user in lista_prestamos:
        print(user.toString())
    input("Presione ENTER para Volver al menu principal...")


def menuPrestamos():
    print("""
Menu prestamos:
1.- Mostrar los prestamos
2.- Agregar un prestamo
3.- Editar un prestamo
4.- Eliminar un prestamo  
    """)
    user_select = input("Ingrese su opcion (1, 2, 3 o 4): ")
    if user_select == "1":
        return mostrarPrestamos()

    elif user_select == "2":
        return new_prestamo()

    elif user_select == "3":
        rut = input("Ingrese el rut del Estudiante/Docente: ")
        return editar_prestamo(rut)

    elif user_select == "4":
        rut = input("Ingrese el rut del Estudiante/Docente: ")
        return eliminar_prestamo(rut)

    else:
        input("Recuerde que debe ingresar una opcion valida...")


# funciones para libros
def mostrarLibros():
    lista_prestamos = mostrar_libros()
    for user in lista_prestamos:
        print(user.toString())
    input("Presione ENTER para Cerrar...")


def libro_nuevo():
    titulo = input("Ingrese el titulo del libro: ")
    cantidad = input("Ingrese la cantidad de libros: ")
    autor = input("Ingrese el nombre del autor: ")
    tipo = input("Ingrese el tipo del libro: ")
    codigo = input("Ingrese el codigo del libro: ")
    book = Libro(titulo, cantidad, autor, tipo, codigo)
    agregar_libro(book)


def menuLibros():
    print("""
Menu Libros:
1.- Mostrar los Libros
2.- Agregar un libro
3.- Editar un libro
4.- Eliminar un libro""")
    user_select = input("Ingrese su opcion (1, 2, 3 o 4): ")
    if user_select == "1":
        return mostrarLibros()

    elif user_select == "2":
        return libro_nuevo()

    elif user_select == "3":
        codigo = input("Ingrese el codigo del libro: ")
        return editar_libro(codigo)

    elif user_select == "4":
        codigo = input("Ingrese el codigo del libro: ")
        return eliminar_libro(codigo)

    else:
        input("Recuerde que debe ingresar una opcion valida...")


# Menu Principal
def mainMenu():
    print(""" 
Menu Principal
1.- Menu Estudiantes/Docentes
2.- Menu Libros.
3.- Menu Prestamos
    """)
    user_select = input("Ingrese su opcion(1,2 o 3): ")
    if user_select == "1":
        menuClientes()
        mainMenu()

    elif user_select == "2":
        menuLibros()
        mainMenu()

    elif user_select == "3":
        menuPrestamos()
        mainMenu()

    else:
        input("\nRecuerde solo ingresar una opcion valida...")
        mainMenu()


mainMenu()