import sqlite3

def contar_clientes():
    """Retorna el número de cliente"""
    try:
        db = sqlite3.connect("linioexp_parcial.db")
        lista_resultado = None
        cursor = db.cursor()
        query = "SELECT COUNT(*) FROM cliente;"
        cursor.execute(query)
        #Se espera un solo resultado
        lista_resultado = cursor.fetchone()
    except Exception as e:
        raise e
    finally:
        db.close()

    return lista_resultado

def mostrar_conteo_clientes(lista):
    if lista is not None:
        for elemento in lista:
            print(elemento)

lista = contar_clientes()
mostrar_conteo_clientes(lista)
