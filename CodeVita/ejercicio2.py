# Día de los deportes
# Descripción del problema
# Una escuela primaria organiza muchos juegos el día deportivo anual. Chintu quería participar y ganar al menos en uno de los juegos. Actualmente, asiste a juegos de resolución de acertijos y pruebas de coeficiente intelectual.

# En la primera ronda se le proporcionan N números enteros que consisten en números positivos y negativos, y se le pide que seleccione tantos como quiera, de modo que la eficiencia resultante de todos los números sea máxima.

# Las reglas para calcular la eficiencia de los números son las siguientes:

# Seleccione tantos números como desee de los números proporcionados (uno, pocos o todos).
# Asigna una prioridad a todos esos números. La prioridad debe variar de uno a K, donde K es el recuento de números que seleccionó.
# La eficiencia es la suma de todos los números multiplicados con sus respectivas prioridades.
# Ayuda a Chintu a calcular la eficiencia máxima que puede lograr utilizando los números dados.

# Restricciones
# 1 <= número de elementos que se le dan <= 10^3

# -10^3 <= cada elemento <= 10^3

# Aporte
# Línea única que consta de todos los números que proporciona Chintu.

# Producción
# Imprime la máxima eficiencia que puede lograr usando los números dados. Imprima cero en caso de que la eficiencia máxima sea negativa.

# Límite de tiempo (segundos)
# 1

# Ejemplos
# Ejemplo 1

# Aporte

# -7 -8 -5 5 -1 -2 0 3

# Producción

# 33

# Explicación

# Seleccione 5, -1, -2, 0, 3 y dé las prioridades, -2 = 1, -1 = 2, 0 = 3, 3 = 4, 5 = 5, entonces la eficiencia será -2*1 + - 1*2 + 0*3 + 3*4 + 5*5 = 33 que es la máxima eficiencia de todas las posibles.

# Ejemplo 2

# Entrada 2

# 4 2 0 -3 -7

# Producción

# 19

# Seleccione 4, 2, 0, -3 y dé las prioridades, -3 = 1, 0 = 2, 2 = 3, 4 = 4, entonces la eficiencia será -3*1 + 0*2 + 2*3 + 4* 4 = 19, que es el máximo de todas las eficiencias posibles.
lista=input("")
lista_numero=lista.split()
lista=[int(numero) for numero in lista_numero]
lista.sort()
suma=0
mayor=0
while len(lista)>0:
    for i,element in enumerate(lista):
        suma+=element*(i+1)
    lista.remove(lista[0])
    if suma>mayor:
        mayor=suma
        suma=0
    suma=0
print(mayor)