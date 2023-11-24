import random

#funcion principal que recibe la lista
def bubble_sort(lista):
    #definimos nuestro switch y la longitud de la lista
    n = len(lista)
    cambios_realizados = True
    
    while cambios_realizados:
        #esto nos asegura que volvamos a recorrer la lista solo si hubo un cambio antes
        #y se necesita un retroceso
        cambios_realizados = False
        #con este for recorremos toda la lista
        for i in range(n - 1):
            #vamos comparando el elemento i con su elemento de adelante
            if lista[i] > lista[i + 1]:
                #si es menor invertimos i por el siguiente y siguiente por i
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                #con esto nos aseguramos que volvamos a recorrer la lista para ir comparando
                cambios_realizados = True

    return lista
if __name__=="__main__":
    #creamos una lista
    lista=[]
    #rellenamos la lista con numeros aleatorios
    for i in range(11):
        lista.append(random.randint(1,101))    
    print(f"Esta es la lista desordenada: {lista},\n Esta es la lista ordenada: {bubble_sort(lista)}")

