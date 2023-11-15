def fnS3(n):
    suma=0
    if n==1:
        return 3
    else:
        suma= (3*n)+fnS3(n-1)
        return suma 
def main():
    suma=fnS3(5)
    print(f"La sumatoria de S(5): {suma}")
main()