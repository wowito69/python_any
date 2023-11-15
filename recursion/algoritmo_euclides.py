def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a % b)

if __name__ == "__main__":
    fraccion = input("Ingresa la fraccion con este formato: 00/00:\n ")
    a, b = map(int, fraccion.split('/'))
    if a%b==0:
        print(f"El resultado de la fracción es: {int(a/b)} ")
    else:
        resultado = euclides(a, b)
        print(f"La forma más simple de la fracción es: {a // resultado}/{b // resultado}")


