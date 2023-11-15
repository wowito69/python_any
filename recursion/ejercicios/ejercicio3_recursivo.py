def calcular_an(n):
    if n == 0:
        return 1
    else:
        return 2 * calcular_an(n - 1)
    
for n in range(16):
    resultado = calcular_an(n)
    print(f'a({n}) = {resultado}')
