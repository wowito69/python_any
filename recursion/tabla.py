
def tabla(numero,rango,resultado=0):
    maximo=numero*rango
    if resultado > maximo:
        pass
    else:
        print(resultado)
        resultado=numero+numero
        tabla(numero,rango,resultado)

tabla(5,10)
