def serie(n):
    if(n==1):
        return 5100
    else:
        sumatoria= 5000*(1+0.08/4)+serie(n-1)
        return sumatoria
    
def main():

    n=int(input("Ingresa el valor de n"))
    print(f"El saldo de la cuenta despues de {n} trimestres es = {serie(n)}")

main()
