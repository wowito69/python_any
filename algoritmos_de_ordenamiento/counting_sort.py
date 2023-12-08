import random 

#funcion principal
def counting(lista):
    #nos apoyamos de una nueva lista la cual va a estar acomodada
    nueva_lista=[]
    #nuestro array que nos ayudara a acomodar
    array=[0]*9
    #por cada elemento de nuestra lista a acomodar
    #inicializamos la nueva lista en 0 y marcamos como uno en nuestro array
    #si aparece el numero en nuestra lista
    for element in lista:
        nueva_lista.append(0)
        array[element-1]+=1
        #ahora recorremos todo el array de apoyo haciendo su suma acumulada
    for i in range(len(array)-1):
        array[i+1]+=array[i]
        #por cada elemento de la lista
    for element in lista:
        #indicamos la posicion que va a tener cada elemento de la lista desordenada
        #en la lista ordenada
        #indice es igual al 
        indice=array[element-1]-1
        nueva_lista[indice]=element
        array[element-1]-=1
    print(nueva_lista)
if __name__=="__main__":
    lista=[]
    for i in range(10):
        lista.append(random.randint(1,9))
    print(lista)
    counting(lista)
    