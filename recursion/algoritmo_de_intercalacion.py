import random 
#para utilizar este algoritmo debemos tener dos listas ordenadas 
from quicksort import quicksort

#funcion intercalacion que recibe las dos listas
def intercalacion(lista1,lista2):
    #definimos las dos longitudes de las listas
    longitud1 = len(lista1)
    longitud2 = len(lista2)
    #definimos una tercer lista vacia 
    lista3 = []
    #nuestros dos contadores
    i = 0
    j = 0
    #para no salirnos de rango i y j tienen que ser menores que la longitud de cada lista
    while i < longitud1 and j < longitud2:
        #si el elemento i de la lista 1 es menor que el j de la lista 2
        if lista1[i] < lista2[j]:
            #agregamos el menor y avanzamos 1 en la lista que utilizamos para agregar
            lista3.append(lista1[i])
            i += 1
            #sino hacemos los contrario
        else:
            lista3.append(lista2[j])
            j += 1
    #esto lo usamos para agregar todos los que sobraron ya sea de i o j
    lista3.extend(lista1[i:])
    lista3.extend(lista2[j:])
    #regresamos la lista 3 para darle un uso
    return lista3

if __name__=="__main__":
        #definimos nuestras dos listas
        lista1=[]
        lista2=[]
        #rellenamos nuestras listas con numeros aleatorios
        for i in range(20):
            lista1.append(random.randint(1,40))
            lista2.append(random.randint(1,101))
        #ordenamos las dos listas con tu algoritmo de ordenamiendo de confianza
        lista1=quicksort(lista1)
        lista2=quicksort(lista2)
        #imprimimos las 2 listas y la que creamos
        print(f"{lista1}\n {lista2}\n {intercalacion(lista1,lista2)}")