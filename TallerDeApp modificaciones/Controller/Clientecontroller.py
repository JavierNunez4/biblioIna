from Model.conexionBD import *
from Model.Cliente import *

def listar_clientes():
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = "SELECT * FROM cliente"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        user_data = []
        for row in datos:
            client = Cliente(None, None, None, None, None, None)
            client.setNombre(row[1])
            client.setApellido(row[2])
            client.setContacto(row[3])
            client.setDireccion(row[4])
            client.setOcupacion(row[5])
            client.setRut(row[6])
            user_data.append(client)
        close_connection(cnx, cursor)
        return user_data
    except Exception as e:
        return print("Error!! ")

def buscar_por_rut(rut):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = f"SELECT * FROM cliente WHERE rut ='{rut}'"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        if not datos:
            print("El rut ingresado es incorrecto o no esta registrado.")
        else:
            client = Cliente(None, None, None, None, None, None)
            for row in datos:
                client.setNombre(row[1])
                client.setApellido(row[2])
                client.setContacto(row[3])
                client.setDireccion(row[4])
                client.setOcupacion(row[5])
                client.setRut(row[6])
        close_connection(cnx, cursor)
        return print(client.toString())
    except Exception as e:
        return print("Error!! ")


def agregar_cliente(client):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        name = client.getNombre()
        apellido = client.getApellido()
        contact = client.getContacto()
        direc = client.getDireccion()
        cargo = client.getOcupacion()
        rut = client.getRut()
        datos = (name, apellido, contact, direc, cargo, rut)
        insert = f"""INSERT INTO cliente (Nombre, Apellido, Contacto, Dirección, Ocupación, Rut) 
        VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(insert, datos)
        cnx.commit()
        print("Usuario Guardado")
        close_connection(cnx, cursor)
    except Exception as e:
        print("Error en la inserción... verifique la conexión")


def editar_cliente(rut):
    cnx = get_conex()
    cursor = cnx.cursor()
    try:
        print(""" 
Ingrese el numero de la opcion que desea editar
1.- Nombre        
2.- Apellido
3.- Contacto
4.- Direccion""")
        seleccion_user = input("Seleccion: ")
        seleccion_user = int(seleccion_user)
        lista_datos = ['Nombre', 'Apellido', 'Contacto', 'Dirección']
        cambio = input("Ingrese el nuevo valor: ")
        consulta = f"UPDATE cliente SET {lista_datos[seleccion_user-1]} = '{cambio}' WHERE Rut = '{rut}'"
        cursor.execute(consulta)
        cnx.commit()
        close_connection(cnx, cursor)
    except Exception as e:
        print("El rut ingresado no esta registrado o fue mal ingresado...")


def eliminar_cliente(rut):
    try:
        cnx = get_conex()
        cursor = cnx.cursor()
        consulta = f"DELETE FROM cliente WHERE Rut = '{rut}'"
        cursor.execute(consulta)
        confirmacion = input("¿Esta seguro/a que desea eliminar el usuario?: ")
        confirmacion = confirmacion.upper()
        if confirmacion == "SI" or confirmacion == "SÍ":
            cnx.commit()
            input("Usuario eliminado... Enter para volver al inicio")
        else:
            input("Usuario No eliminado... Enter para volver al inicio")
    except:
        input("Error")