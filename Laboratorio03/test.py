import sqlite3
from producto import Producto
from cliente import Cliente

def consultar_datos(tabla):
    """Recibe el nombre de una tabla como string.
        Devuelve una lista con los datos en la tabla"""

    try:
        #Conexion a la db
        db = sqlite3.connect("linioexp_parcial_lab3.db")
        #Objeto cursor
        cursor = db.cursor()
        query = "SELECT * FROM " + tabla + ";"
        cursor.execute(query)
        resultados = cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        db.close()
    for resultado in resultados:
        print(resultado)

def test_cliente():
    cliente_new = Cliente(email="mauroleonpayano@gmail.com", password="demo")
    print(cliente_new.crear_cuenta())
    consultar_datos("clientes")

#test_cliente()
consultar_datos("productos")
