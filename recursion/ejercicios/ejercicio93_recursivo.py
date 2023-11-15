def serie(n,a=3):

    if(n==1):
        return 3
    else:
        serie= a*-3
        a+=a
        serie(n-1)
        return sumatoria
    
def main():

    n=int(input("Ingresa el valor de n"))
    print(f"El saldo de la cuenta despues de {n} trimestres es = {serie(n)}")

main()
