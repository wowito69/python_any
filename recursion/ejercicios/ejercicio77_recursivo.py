def serie(n,i=1):
    if(n<i):
        return 0
    else:
        sumatoria=n**2+serie(n-1,i)
        return sumatoria
    
def main():
    i=int(input("Ingresa el valor de i"))
    n=int(input("Ingresa el valor de n"))
    print(f"Σ(i = {1} a {n}) = {serie(n,i)}")

main()
