import random
class Nodo:
    def __init__(self, valor):
        #definimos su campo dato
        self.valor = valor
        # y sus dos apuntadores izquierda y derecha iniciados en NUll
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz=None):
        #en la estructura arbol solo definimos su raiz en null o si quieres puedes modificarla en el inicio
        self.raiz = raiz

    def insertar(self, valor):
        #si la raiz es null entonces creamos un nodo con el valor indicado en raiz
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            #sino nos apoyamos de otra funcion que nos ayude a acomodarla
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        #si el valor es menor al nodo actual en su campo valor
        if valor < nodo_actual.valor:
            #entonces va a ir a la izquiera
            #si es nulo significa que podemos usar el espacio izquierdo
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            #sino tenemos que llavar a la funcion que nos ayuda a acomodar 
            #de manera recursiva hasta que encuentre un lugar vacio y menor o mayor al anterior
            else:
                self._insertar(valor, nodo_actual.izquierda)
        #si valor es mayor que el valor en el nodo actual va ir a la derecha
        elif valor > nodo_actual.valor:
            #si el nodo apunto en derecha esta vacio
            if nodo_actual.derecha is None:
                #se crea un nodo con el valor indicado y sus apuntadores derecha izuqierda
                nodo_actual.derecha = Nodo(valor)
            #sino se sigue buscando un lugar en el que sea menor o mayor y este vacio
            else:
                self._insertar(valor, nodo_actual.derecha)
        else:
            print("El valor ya existe en el arbol")
            return

    def imprimir_inorder(self, nodo_actual):
        #esta funcion es recursiva por lo que si nodo_actual o sea true(existe)
        if nodo_actual:
            #vamos a llamar a la funcion las veces necesarias para que llegue
            #al ultimo valor izquierdo lo imprima y continue hasta acabar los izquierdo 
            self.imprimir_inorder(nodo_actual.izquierda)
            print(nodo_actual.valor,"<-", end=' ')
            self.imprimir_inorder(nodo_actual.derecha)

    def imprimir_pre_order(self,nodo_actual):
        if nodo_actual:
            
            print(nodo_actual.valor,"<-", end=' ')
            self.imprimir_pre_order(nodo_actual.izquierda)
            self.imprimir_pre_order(nodo_actual.derecha)

def aleatorio():
        numero=0
        for i in range(101):
            numero=random.randint(1,100)
            arbol.insertar(numero)

if __name__ == "__main__":
    arbol = ArbolBinario()
    while True:
        seleccion = int(input("\n¿Qué deseas hacer?\n1.-Agregar Nodo\n2.-Buscar Valor\n3.-Eliminar Valor\n4.-Mostrar en Orden\n5.-Salir\n"))
        if seleccion == 1:
            op=int(input("¿Deseas rellenar de 100 numeros aleatorios?\n1.-Si  2.-No\n"))
            if op==1:
                aleatorio()
                arbol.imprimir_pre_order(arbol.raiz)

            else:
                arbol.insertar(int(input("Que valor deseas agregar")))
                arbol.imprimir_pre_order(arbol.raiz)
        # elif seleccion == 2:
        #     lista.buscar_valor(int(input("Qué valor deseas buscar: ")))
        # elif seleccion == 3:
        #     arbol.eliminar_valor(int(input("Qué valor deseas eliminar: ")),arbol.raiz)
        elif seleccion == 4:
                print("Recorrido Inorden:")
                arbol.imprimir_inorder(arbol.raiz)
        elif seleccion == 5:
            print("\nSaliendo...")
            break
