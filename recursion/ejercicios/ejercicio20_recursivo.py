def serie(n):
    if(n==0):
        return 0
    else:
        valor=n*(n-1)*(n-2)
        serie(n-1)
        print("Valor ", n ," = ",valor)
        return valor
    
def main():
    serie(15)

main()