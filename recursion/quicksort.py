import random
#inicio de la funcion
def quicksort(array):
    #comprobamos si su longitud es menor o igual a uno, ya que en este caso ya estaria ordenada
    if len(array)<=1:
        return array
    #seleccionamos un pivote y creamos el conjunto menor al pivote y el mayor al pivote
    pivote=array[-1]
    izquierda=[]
    derecha=[]
    # exploramos el array de el primer elemento hasta el pivote excluyendo a este 
    for i in array[:-1]:
        # si el elemento es menor o igual al pivote lo enviamos a el conjunto izquierdo(menor que pivote)
        if i <= pivote:
            izquierda.append(i)
        # sino mandamos el elemento al conjunto derecho(mayor que el pivote)
        else:
            derecha.append(i)
    # luego volvemos a llamar la funcion enviando como parametro los dos arrays creados con los elementos mayores y menores que el pivote
    quick_izquierda=quicksort(izquierda)
    quick_derecha=quicksort(derecha)
    #despues de que termine cada llamado a la funcion, juntamos el array que dividimos en 3 pero ya acomodado
    return quick_izquierda+[pivote]+quick_derecha
# se llama a la funcion y a la par se imprime
if __name__=="__main__":
    lista=[]
    for i in range(11):
        lista.append(random.randint(1,101))    
    print(f"Esta es la lista desordenada: {lista}\nEsta es la lista ordenada: {quicksort(lista)}")


