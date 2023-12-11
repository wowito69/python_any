k =1 
lista=input()
lista_numero=lista.split()
lista=[int(numero) for numero in lista_numero]
bolsa=int(input())
lista.sort(reverse=True)
cambios=True
for i in range(len(lista)):
    if len(lista)==1 and bolsa>lista[0]:
        bolsa-=lista[-1]
        k+=1
        mayor=k
        lista.remove(lista[-1])
        cambios=False
    elif len(lista)==0:
        break
    else:
        if cambios:
            if lista[-1]<=bolsa:
                bolsa-=lista[-1]
                k+=1
                mayor=k
                lista.remove(lista[-1])
                cambios=False
            else:
                pass
        else:
            if lista[0]>bolsa:
                bolsa+=lista[0]
                k-=1
                lista.remove(lista[0])
                cambios=True

print(mayor)