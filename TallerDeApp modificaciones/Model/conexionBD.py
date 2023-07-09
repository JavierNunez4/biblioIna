import mysql.connector as sql

def get_conex():
    try:       
        conection = sql.connect(user='admin', password='admin', host='127.0.0.1', database='prueba', port='3306')
        return conection
    except Exception as error:
        return print("Error de conexion  :",  error)
def close_connection(cnx, cursor):
    if cnx:
        cursor.close()
        cnx.close()


    
