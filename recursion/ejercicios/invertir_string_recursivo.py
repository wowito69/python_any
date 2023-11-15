cadena_invertida = ""

def invertir(cadena):
    global cadena_invertida
    if len(cadena) == 1:
        cadena_invertida += cadena
        return cadena_invertida
    else:
        cadena_invertida += cadena[-1]
        invertir(cadena[ :-1])

def main():
    cadena = input("Introduce la cadena que quieres invertir: ")
    invertir(cadena)
    print(f"La cadena original es: {cadena} y la inversa es: {cadena_invertida}")
main()

def main():
    cadena = input("Introduce la cadena que quieres invertir: ")
    invertir(cadena)


def invertir(cadena):
    for i in range(len(cadena)-1,-1,-1):
        print(cadena[i],end="")
        
main()