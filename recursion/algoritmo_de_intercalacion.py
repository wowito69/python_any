import random 
from quicksort import quicksort

def intercalacion(lista1,lista2):
    longitud1 = len(lista1)
    longitud2 = len(lista2)
    lista3 = []

    i = 0
    j = 0

    while i < longitud1 and j < longitud2:
        if lista1[i] < lista2[j]:
            lista3.append(lista1[i])
            i += 1
        else:
            lista3.append(lista2[j])
            j += 1

    lista3.extend(lista1[i:])
    lista3.extend(lista2[j:])
    return lista3
if __name__=="__main__":
        lista1=[]
        lista2=[]
        for i in range(20):
            lista1.append(random.randint(1,40))
            lista2.append(random.randint(1,101))
        lista1=quicksort(lista1)
        lista2=quicksort(lista2)
        print(f"{lista1}\n {lista2}\n {intercalacion(lista1,lista2)}")