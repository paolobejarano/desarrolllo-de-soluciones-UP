import sqlite3

def obtener_resultado2():
    """Retorna el número de cliente"""
    try:
        db = sqlite3.connect("linioexp_parcial.db")
        lista_resultado = None
        cursor = db.cursor()
        query = "SELECT * FROM pedido, cliente WHERE pedido.id_cliente = cliente.id_cliente AND pedido.distrito = 'CALLAO'"
        cursor.execute(query)
        # Se espera un solo resultado
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

lista = obtener_resultado2()
mostrar_resultados(lista)
