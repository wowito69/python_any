import random
def eliminar(array,matriz,i,j,dele):
    eliminados=[]
    if j>=3 and j<6:
        for j in range(3):
            if matriz[i][j] not in dele and matriz[i][j] not in array:
                pass
            elif matriz[i][j] in array:
                eliminados.append(matriz[i][j])
                array.remove(matriz[i][j])
    elif j>=6:
        for j in range(6):
            if matriz[i][j] not in dele and matriz[i][j] not in array:
                    pass
            elif matriz[i][j] in array:
                    eliminados.append(matriz[i][j])
                    array.remove(matriz[i][j])
    return array,True,eliminados

def asignar_numero(array,i,j):
        if len(array)!=0:
            n=random.randint(0,len(array)-1)
            matriz[i][j]=array[n]
            array.remove(matriz[i][j])

def agregar(matriz):
    for x in range(9):
        for y in range(9):
            if x<3 and y<3:
                array=[1,2,3,4,5,6,7,8,9]
                for i in range(3):
                    for j in range(3):
                        asignar_numero(array,i,j)
            elif x<3 and y<6 and y>=3:
                array=[1,2,3,4,5,6,7,8,9]
                eliminados=[]
                cambios=False
                for i in range(3):
                    for j in range(3,6):
                        if cambios:
                            asignar_numero(array,i,j)
                        else:
                            array,cambios,eliminados=eliminar(array,matriz,i,j,eliminados)
                            asignar_numero(array,i,j)
                    cambios=False
                    array+=eliminados
                    eliminados=[]
            elif y>=6 and x<3:
                array=[1,2,3,4,5,6,7,8,9]
                eliminados=[]
                cambios=False
                for i in range(3):
                    for j in range(6,9):
                        if cambios:
                            asignar_numero(array,i,j)
                        else:
                            array,cambios,eliminados=eliminar(array,matriz,i,j,eliminados)
                            asignar_numero(array,i,j)
                    cambios=False
                    array+=eliminados
                    eliminados=[]

            elif x>=3 and x<6 and y<3:
                for i in range(3,6):
                    for j in range(3):
                        matriz[i][j]=0
            elif x>=3 and x<6 and y>=3 and y<6:
                for i in range(3,6):
                    for j in range(3,6):
                        matriz[i][j]=0
            elif y>=6 and x<6 and x>=3:
                for i in range(3,6):
                    for j in range(6,9):
                        matriz[i][j]=0 

            elif x>=6 and y<3:
                for i in range(6,9):
                    for j in range(3):
                        matriz[i][j]=0
            elif x>=6 and y>=3 and y<6:
                for i in range(6,9):
                    for j in range(3,6):
                        matriz[i][j]=0 
            elif y>=6 and x>=6:
                for i in range(6,9):
                    for j in range(6,9):
                        matriz[i][j]=0                     
filas = 9
columnas = 9
matriz = [[0] * columnas for _ in range(filas)]
agregar(matriz)
for fila in matriz:
    print(fila)