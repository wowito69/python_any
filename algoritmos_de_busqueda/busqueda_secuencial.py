import random

#funcion busqueda
def busqueda_secuencial(lista, busqueda):
    #esta funcion va a ir iterando por cada elemento de la lista y comparando
    for i, element in enumerate(lista):
        #si el elemento es igual a la busqueda entonces devuelve el indice
        if element == busqueda:
            return i
    #si termino de recorrerla y no coincidio entonces no se encuentra en la lista
    print("El elemento no se encuentra en la lista")

if __name__ == "__main__":
    #lista
    lista = []
    #rellenamos de 10 numeros aleatorios
    for i in range(10):
        lista.append(random.randint(1, 100))
    print(f"Esta es la lista: {lista}")
    #llamamos a la funcion
    busqueda = int(input('Ingresa el numero el cual quieres buscar: '))
    #guardamos la posicion para usarla de algun modo
    posicion = busqueda_secuencial(lista, busqueda)

    #si la funcion regreso algo entonces imprimimos la posicion
    if posicion is not None:
        print(f"El elemento se encuentra en la posición {posicion}")
