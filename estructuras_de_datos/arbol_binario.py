import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(valor, nodo_actual.derecha)
        else:
            print("El valor ya existe en el árbol")
            return

    def imprimir_inorder(self, nodo_actual):
        if nodo_actual:
            self.imprimir_inorder(nodo_actual.izquierda)
            print(nodo_actual.valor, "<-", end=' ')
            self.imprimir_inorder(nodo_actual.derecha)

    def imprimir_pre_order(self, nodo_actual):
        if nodo_actual:
            print(nodo_actual.valor, "<-", end=' ')
            self.imprimir_pre_order(nodo_actual.izquierda)
            self.imprimir_pre_order(nodo_actual.derecha)

    def eliminar_valor(self, actual, valor, anterior):
        if actual is not None:
            if actual.valor == valor:
                if actual.izquierda is None and actual.derecha is None:
                    if anterior is not None:
                        if anterior.izquierda == actual:
                            anterior.izquierda = None
                        else:
                            anterior.derecha = None
                    else:
                        self.raiz = None
                    print("Listo")
                elif (actual.izquierda is None and actual.derecha is not None) or (actual.derecha is None and actual.izquierda is not None):
                    if anterior is not None:
                        if anterior.izquierda == actual:
                            anterior.izquierda = actual.izquierda or actual.derecha
                        else:
                            anterior.derecha = actual.izquierda or actual.derecha
                    else:
                        self.raiz = actual.izquierda or actual.derecha
                    print("Listo")
                else:
                    if anterior is not None:
                        self.recorrer_derecho_izquierda(actual.derecha, anterior, actual)
                    else:
                        self.recorrer_derecho_derecha(actual.derecha, anterior, actual)
            self.eliminar_valor(actual.izquierda, valor, actual)
            self.eliminar_valor(actual.derecha, valor, actual)

    def recorrer_derecho_izquierda(self, ultimo_izquierdo, anterior_de_borrar, a_borrar):
        if ultimo_izquierdo.izquierda is not None:
            self.recorrer_derecho_izquierda(ultimo_izquierdo.izquierda, anterior_de_borrar, a_borrar)
        else:
            anterior_de_borrar.izquierda = ultimo_izquierdo
            if ultimo_izquierdo.derecha is not None:
                ultimo_izquierdo.derecha = a_borrar.derecha

    def recorrer_derecho_derecha(self, ultimo_izquierdo, anterior_de_borrar, a_borrar):
        if ultimo_izquierdo.izquierda is not None:
            self.recorrer_derecho_derecha(ultimo_izquierdo.izquierda, anterior_de_borrar, a_borrar)
        else:
            anterior_de_borrar.derecha = ultimo_izquierdo
            if ultimo_izquierdo.derecha is not None:
                ultimo_izquierdo.derecha = a_borrar.derecha


def aleatorio(arbol):
    for i in range(101):
        numero = random.randint(1, 100)
        arbol.insertar(numero)

if __name__ == "__main__":
    arbol = ArbolBinario()
    while True:
        seleccion = int(input("\n¿Qué deseas hacer?\n1.-Agregar Nodo\n2.-Buscar Valor\n3.-Eliminar Valor\n4.-Mostrar en Orden\n5.-Salir\n"))
        if seleccion == 1:
            op = int(input("¿Deseas rellenar de 100 numeros aleatorios?\n1.-Si  2.-No\n"))
            if op == 1:
                aleatorio(arbol)
                arbol.imprimir_pre_order(arbol.raiz)
            else:
                arbol.insertar(int(input("Qué valor deseas agregar: ")))
                arbol.imprimir_pre_order(arbol.raiz)
        elif seleccion == 3:
            arbol.eliminar_valor(arbol.raiz, int(input("Qué valor deseas eliminar: ")), None)
            arbol.imprimir_inorder(arbol.raiz)
        elif seleccion == 4:
            print("Recorrido Inorden:")
            arbol.imprimir_inorder(arbol.raiz)
        elif seleccion == 5:
            print("\nSaliendo...")
            break
