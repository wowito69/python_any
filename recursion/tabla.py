
def tabla(numero,rango=10,resultado=0):
    maximo=numero*rango
    if resultado > maximo:
        return
    else:
        print(f"El resultado de {numero}x{int(resultado/numero)} es : {resultado}")
        resultado+=numero
        tabla(numero,rango,resultado)

if __name__=="__main__":
    tabla(int(input("El numero de el que deseas la tabla: ")))
