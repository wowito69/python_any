def fnS4(n):
    suma=0
    if n==2:
        return 20
    else:
        suma=3+(fnS4(n-1))*2(fnS4(n-1))
        return suma
    
def main():
    print("La sumatoria es:",fnS4(6))
main()
