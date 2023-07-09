from Model.Prestamo import *
from Model.conexionBD import *
from datetime import datetime

def mostrar_prestamos():
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = "SELECT * FROM prestamos"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        user_data = []
        for row in datos:
            prestamo = Prestamos()
            prestamo.setRutCliente(row[1])
            prestamo.setEstado(row[2])
            prestamo.setFechaEntrega(row[3])
            prestamo.setFechaDev(row[4])
            prestamo.setTitulo(row[5])
            user_data.append(prestamo)
        close_connection(cnx, cursor)
        return user_data
    except Exception as e:
        return print("Error!! ")


def get_cargo(rut_cliente):
    cnx = get_conex()
    cursor = cnx.cursor()
    query_cargo = f""" SELECT Ocupación FROM cliente WHERE Rut ='{rut_cliente}' """
    cursor.execute(query_cargo)
    cargo = cursor.fetchone()
    return cargo[0]


def get_fechaentrega(rut_cliente, fecha_prestamo):
    cnx = get_conex()
    cursor = cnx.cursor()
    cargo = get_cargo(rut_cliente)
    if cargo == "Alumno":
        query_entrega = f"SELECT adddate('{fecha_prestamo}',interval 7 day)"
        cursor.execute(query_entrega)
        fecha_entrega = cursor.fetchone()
        fecha_entrega = fecha_entrega[0]
        close_connection(cnx, cursor)
        return fecha_entrega
    elif cargo == "Docente":
        query_entrega = f"SELECT adddate('{fecha_prestamo}',interval 20 day)"
        cursor.execute(query_entrega)
        fecha_entrega = cursor.fetchone()
        fecha_entrega = fecha_entrega[0]
        close_connection(cnx, cursor)
        return fecha_entrega


def new_prestamo():
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        rut_cliente = input("Ingrese el Rut del estudiante/docente: ")
        estado = "al dia"
        titulo = input("Ingrese el titulo del libro: ")
        codigo = input("Ingrese el codigo del libro: ")
        fecha_prestamo = datetime.now().date()
        fecha_entrega = get_fechaentrega(rut_cliente, fecha_prestamo)
        insert = f"""INSERT INTO prestamos (Rut_cliente, Estado_libro, Fecha_prestamo,Fecha_entrega,Titulo_libro, codigo)
            VALUES ('{rut_cliente}','{estado}','{fecha_prestamo}','{fecha_entrega}','{titulo}','{codigo}')"""
        cursor.execute(insert)
        cnx.commit()
        print("Prestamo Guardado")
        close_connection(cnx, cursor)
        input("Enter para volver al menu...")
    except SyntaxError as e:
        return print("El rut del usuario debe estar registrado antes...")

def editar_prestamo(rut):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        print(""" 
Ingrese el numero de la opcion que desea editar
1.- Estado del libro      
2.- Fecha de entrega""")
        seleccion_user = input("Ingrese el numero de la opcion que desea editar: ")
        seleccion_user = int(seleccion_user)
        cambio = input("Ingrese el nuevo valor: ")
        lista_datos = ["Estado_libro", "Fecha_entrega"]
        query = f"UPDATE prestamos SET {lista_datos[seleccion_user-1]} = '{cambio}' WHERE Rut_cliente = '{rut}'"
        cursor.execute(query)
        cnx.commit()
        close_connection(cnx, cursor)
    except Exception as e:
        input("Error... ")


def eliminar_prestamo(rut):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = f"DELETE FROM prestamos WHERE Rut_cliente = '{rut}'"
        cursor.execute(consulta)
        confirmacion = input("¿Esta seguro/a que desea eliminar el prestamo?: ")
        confirmacion = confirmacion.upper()
        if confirmacion == "SI" or confirmacion == "SÍ":
            cnx.commit()
            input("El prestamo fue eliminado. Pulse enter para Volver al menu principal")
        else:
            pass
    except Exception as e:
        print("Error")

