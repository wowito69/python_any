import math

array = [17, 26, 33, 42, 53, 60, 60, 71, 89, 98]

def busqueda_binaria(array, busqueda):
    if not array:
        print(f"El valor {busqueda} no se encuentra en la lista.")
        return

    media = math.floor(len(array) / 2)
    valor_medio = array[media]

    if busqueda < valor_medio:
        return busqueda_binaria(array[:media], busqueda)
    elif busqueda > valor_medio:
        return busqueda_binaria(array[media + 1:], busqueda)
    else:
        print(f"El valor {busqueda} se encuentra en la posición {media}.")

busqueda = int(input("Valor a buscar: "))
busqueda_binaria(array, busqueda)
