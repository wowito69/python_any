#nuestra funcion euclides recibe el numerador y denominador 
def euclides(a, b):
    #si b(el residuo de la division anterior de a y b) es igual a 0
    #nos quedamos con a como maximo comun divisior
    if b == 0:
        return a
    else:
    #sino llamamos de manera recursiva mandando ahora como numerador a b y como denominador el residuo de la division de a/b
        return euclides(b, a % b)

if __name__ == "__main__":
    #preguntamos la fraccion a simplificas
    fraccion = input("Ingresa la fraccion con este formato: 00/00:\n ")
    #guardamos en a y b dividos por /
    a, b = map(int, fraccion.split('/'))
    #si a y b al dividir a entre b el residuo es 0, regresamos la division de a/b
    if a%b==0:
        print(f"El resultado de la fracción es: {int(a/b)} ")
    else:
        #sino conseguimos nuestro divisor 
        resultado = euclides(a, b)
        #y aqui imprimimos diviendo cada uno entre su divisior para que quede simplificada
        print(f"La forma más simple de la fracción es: {a // resultado}/{b // resultado}")


