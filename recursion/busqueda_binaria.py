import math
#este algoritmo necesita de una lista previamente ordenada 
#asi que aqui la definimos
array = [17, 26, 33, 42, 53, 60, 60, 71, 89, 98]

#nuestra funcion principal que recibe la lista y la busqueda
def busqueda_binaria(array, busqueda):
    #si no se encuentra imprimimos eso
    if not array:
        print(f"El valor {busqueda} no se encuentra en la lista.")
        return
    #este algoritmo necesita dividir la lista en dos
    media = math.floor(len(array) / 2)
    #y utilizamos como pivote el valor que se encuentre en medio
    valor_medio = array[media]
    #si la busqueda es menor que nuestro pivote
    if busqueda < valor_medio:
        #llamamos a la funcion de manera recursiva enviando solo la mitad izquierda de la lista
        return busqueda_binaria(array[:media], busqueda)
    #sino enviamos la mitad derecha excluyendo a el pivote antes usado
    elif busqueda > valor_medio:
        return busqueda_binaria(array[media + 1:], busqueda)
    #sino significa que casualmente el pivote tambien es nuestro numero a buscar asi que imprimimos
    else:
        print(f"El valor {busqueda} se encuentra en la posición {media}.")
#preguntamos y llamamos a la funcion
busqueda = int(input("Valor a buscar: "))
busqueda_binaria(array, busqueda)
