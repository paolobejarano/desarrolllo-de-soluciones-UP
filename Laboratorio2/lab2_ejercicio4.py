import sqlite3

def obtener_resultado4():
    """Retorna el número de cliente"""
    try:
        db = sqlite3.connect("linioexp_parcial.db")
        lista_resultado = None
        cursor = db.cursor()
        query = "SELECT producto.nombre, SUM(cantidad) FROM linea_pedido INNER JOIN producto ON linea_pedido.id_producto = producto.id_producto GROUP BY linea_pedido.id_producto HAVING SUM(cantidad) = (SELECT SUM(cantidad) FROM linea_pedido GROUP BY linea_pedido.id_producto ORDER BY SUM(cantidad) DESC LIMIT 1)"
        cursor.execute(query)
        #Se esperan varios resultados y no se sabe la cantidad, por lo tanto, se usa fetchall
        lista_resultado = cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        db.close()

    return lista_resultado

def mostrar_resultados(lista):
    if lista is not None:
        for elemento in lista:
            print(elemento)

lista = obtener_resultado4()
mostrar_resultados(lista)
