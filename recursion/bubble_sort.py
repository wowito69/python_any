import random
def bubble_sort(lista):
    n = len(lista)
    cambios_realizados = True

    while cambios_realizados:
        cambios_realizados = False
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambios_realizados = True

    return lista
if __name__=="__main__":
    lista=[]
    for i in range(11):
        lista.append(random.randint(1,101))    
    print(f"Esta es la lista desordenada: {lista},\n Esta es la lista ordenada: {bubble_sort(lista)}")

