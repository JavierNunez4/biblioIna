from Model.conexionBD import *
from Model.Libro import *


def mostrar_libros():
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = "SELECT * FROM libro"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        user_data = []
        for row in datos:
            libro = Libro(None, None, None, None, None)
            libro.setTitulo(row[1])
            libro.setTipo(row[4])
            libro.setAutor(row[3])
            libro.setCantidad(row[2])
            libro.setCodigo(row[5])
            user_data.append(libro)
        close_connection(cnx, cursor)
        return user_data
    except Exception as e:
        return input("Error!! ")


def agregar_libro(libro):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        titulo = libro.getTitulo()
        cantidad = libro.getCantidad()
        autor = libro.getAutor()
        tipo = libro.getTipo()
        codigo = libro.getCodigo()
        datos = (titulo, cantidad, autor, tipo, codigo)
        insert = f"""INSERT INTO libro (Titulo_libro, Cantidad, Autor, Tipo, Código) 
        VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(insert, datos)
        cnx.commit()
        input("Usuario Guardado... Enter para volver")
        close_connection(cnx, cursor)
    except SyntaxError as e:
        input("Error en la inserción... verifique la conexión")


def editar_libro(codigo):
    cnx = get_conex()
    cursor = cnx.cursor()
    try:
        print(""" 
Ingrese el numero de la opcion que desea editar
1.- Titulo     
2.- Cantidad
3.- Autor
4.- Tipo""")
        seleccion_user = input("Seleccion: ")
        seleccion_user = int(seleccion_user)
        cambio = "Ingrese el nuevo valor: "
        lista_datos = ['Titulo_libro', 'Cantidad', 'Autor', 'Tipo']
        consulta = f"UPDATE libro SET {lista_datos[seleccion_user - 1]} = '{cambio}' WHERE Código = '{codigo}'"
        cursor.execute(consulta)
        cnx.commit()
        close_connection(cnx, cursor)
    except Exception as e:
        input("El Codigo ingresado no esta registrado o fue mal ingresado...")


def eliminar_libro(codigo):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = f"DELETE FROM libro WHERE Código = '{codigo}'"
        cursor.execute(consulta)
        confirmacion = input("¿Esta seguro/a que desea eliminar el libro?: ")
        confirmacion = confirmacion.upper()
        if confirmacion == "SI" or confirmacion == "SÍ":
            cnx.commit()
            close_connection(cnx, cursor)
        else:
            pass
    except:
        input("Error")