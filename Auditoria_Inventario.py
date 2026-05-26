# Problema 3 - Auditoría de Inventario y Reabastecimiento
# Estudiante: Victor Manuel Gomez Arce
# Universidad Nacional abierta y a distancia-UNAD
# Escuela de Ciencias Básicas, Tecnología e Ingeniería ECBTI
# Fundamentos De Programación
# Codigo Autoria Propia

# Definición de índices para las columnas de la matriz de inventario#

IDX_CODIGO = 0
IDX_NOMBRE = 1
IDX_STOCK_ACTUAL = 2
IDX_STOCK_MINIMO = 3


def cantidad_a_pedir(stock_actual, stock_minimo):
    "Determina la cantidad exacta a pedir para un artículo."
  
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


def generar_lista_pedidos(inventario):
    "Genera una lista de pedidos a partir de la matriz de inventario."

  
    pedidos = []

    for articulo in inventario:
        nombre = articulo[IDX_NOMBRE]
        stock_actual = articulo[IDX_STOCK_ACTUAL]
        stock_minimo = articulo[IDX_STOCK_MINIMO]

        pedir = cantidad_a_pedir(stock_actual, stock_minimo)

        if pedir > 0:
            pedidos.append((nombre, pedir))

    return pedidos


def imprimir_pedidos(pedidos):
    "Imprime la lista de pedidos en pantalla."

  
    print("\n=== LISTA DE PEDIDOS (REABASTECIMIENTO) ===")

    if len(pedidos) == 0:
        print("No hay artículos por reabastecer. Todo el inventario está al día.")
        return

    for nombre, cantidad in pedidos:
        print(f"- {nombre}: pedir {cantidad} unidad(es)")


def main():
    """Función principal: define la matriz, genera pedidos y los imprime."""

    # Matriz con articulos y sus datos: [Código, Nombre, Stock Actual, Stock Mínimo]
    inventario = [
        ["A001", "Arroz", 8, 15],
        ["A002", "Azúcar", 2, 10],
        ["A003", "Aceite", 5, 12],
        ["A004", "Café", 1, 12],
        ["A005", "Harina", 3, 8],
    ]

    # Generar pedidos usando la lógica de negocio
    pedidos = generar_lista_pedidos(inventario)

    # Mostrar salida solicitada
    imprimir_pedidos(pedidos)


if __name__ == "__main__":
    main()
