import sqlite3

def obtener_resultado3():
    """Retorna el número de cliente"""
    try:
        db = sqlite3.connect("linioexp_parcial.db")
        lista_resultado = None
        cursor = db.cursor()
        query = "SELECT cliente.nombres, cliente.apellidos, SUM(pedido.precio_total) FROM pedido INNER JOIN cliente ON cliente.id_cliente = pedido.id_cliente GROUP BY pedido.id_cliente HAVING SUM(pedido.precio_total) = (SELECT SUM(precio_total) FROM pedido GROUP BY pedido.id_cliente ORDER BY SUM(precio_total) DESC LIMIT 1)"
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

lista = obtener_resultado3()
mostrar_resultados(lista)
