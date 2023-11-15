import random
#creamos la clase nodo
class Nodo:
    def __init__(self, dato):
        #creamos dos campos: siguiente y dato
        self.dato = dato
        self.siguiente = None

#creamos la clase de la lista
class ListaEnlazada:
    def __init__(self):
        #definimos nuestro inicio
        self.cabeza = None
    
    
    def agregar_nodo(self, dato):
        #creamos una instancia de nuestra clase nodo, o sea un nodo con el dato que nos proporcionaron
        nuevo_nodo = Nodo(dato)
        #preguntamos si nuestra lista esta vacia y en caso de estarlo agregamos nuestro nodo al inicio
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        #en caso de que nuestra lista no este vacia
        else:
            #empezamos en inicio
            actual = self.cabeza
            #la recorremos nodo por nodo mientras sea diferente de null-none
            while actual.siguiente is not None:
                #si no es null no nos sirve para meter datos asi que pasamos al siguiente nodo
                actual = actual.siguiente
            #cuando salgamos de el while sabremos que se rompio la condicion asi que nuestro nodo siguiente era null asi que podemos ocuparlo
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        #nos colocamos en el nodo del inicio
        actual = self.cabeza
        #vamos nodo por nodo imprimiendo
        while actual is not None:
            print(actual.dato, "->", end=" ")
            actual = actual.siguiente
        #nuestro final de la lista nunca esta indicado pero sabemos que siempre apunta a null-none
        print("None")

    def buscar_valor(self,dato):
        #nos ubicamos al inicio
        actual=self.cabeza
        #recorremos nodo por nodo solo si el nodo no esta vacio
        while actual is not None:
            #si el nodo no esta vacio nos aseguramos que el nodo en su campo dato sea igual al dato que estamos buscando
            if actual.dato == dato:
                #imprimos y regresamos
                print("\nEl elemento si se encuentra en la lista")
                return
            #sino hay que seguir buscando en el siguiente nodo
            actual=actual.siguiente
        #ya que recorrimos toda la lista hasta llegar a null y el valor no coincidio, damos por hecho que el elemento no se encuentra en la lista
        print("\nEl elemento no se encuentra en la lista")

    def eliminar_valor(self, dato):
        #nos ubicamos al inicio
        actual = self.cabeza
        #y creamos un apuntador apuntando a nada
        anterior = None
        #si el actual osea el primero no es nulo y ademas su dato es igual al que queremos eliminar
        if actual is not None and actual.dato == dato:
            #solo nuestro inicio sera ahora el siguiente de nuestro nodo actual(inicio)
            self.cabeza = actual.siguiente
            print("\nEl elemento se ha eliminado")
            return
        
        #ahora en el caso que no sea el primero, exploramos uno por uno descartandolo si es null
        while actual is not None:
            #si el campo dato de nuestro nodo actual es igual al valor que queremos eliminar
            if actual.dato == dato:
                # entonces el siguiente de el elemento anterior o sea el actual ahora es el siguiente de el elemento actual
                anterior.siguiente = actual.siguiente
                print("\nEl elemento se ha eliminado")
                return
            #sino avanzamos uno el actual y el anterior se lo damos a actual
            anterior = actual
            actual = actual.siguiente
        #si nada de lo anterior funciono damos por hecho que no esta en la lista
        print("\nEl elemento no se encuentra en la lista")

    def modificar_valor(self,dato):
        #iniciamos a la cabeza de la lista 
        actual=self.cabeza
        #exploramos toda la lista
        while actual is not None:
            #si el campo dato en el nodo actual es igual al dato que vamos a modificar
            if actual.dato == dato:
                #pedimos el numero por el cual se va a modificar
                modificacion = int(input("Ingresa el nuevo valor: "))
                #actual en su campo dato ahora es igual a modificacion
                actual.dato=modificacion
                print(f"\nEl numero {dato} se ha modificado por el {modificacion}")
                #regresamos
                return
            #sino seguimos buscando en el nodo siguiente
            actual=actual.siguiente
        #en caso de que se salga de el while y no fue por el return signica que no se encontro
        print("\nEl elemento no se encuentra en la lista")
    
    #no quiero ordenar un dato cada que entre asi que mejor una opcion para acomodarlo cada que queramos
    def acomodar_quicksort(self):
        # primero la lista enlazada a una lista de python para aplicar el ordenamiento quick
        lista = []
        # me situo en el inicio
        actual = self.cabeza
        while actual is not None:
            #cada campo dato lo voy agregando a mi lista de python
            lista.append(actual.dato)
            # y avanzo al siguiente nodo
            actual = actual.siguiente
        
        # llamo a mi función de quick para ordenar la lista
        lista = self.quicksort(lista)
        
        # reconstruyo mi lista enlazada a partir de la lista de python ordenada
        #inicio mi inicio en none
        self.cabeza = None
        # y por cada elemento de mi lista ordenada de python yo mando llamar a mi funcion agregar nodo de mi clase lista enlazada
        for dato in lista:
            self.agregar_nodo(dato)

    # mi funcion quick
    def quicksort(self, array):
        #comprobamos si su longitud es menor o igual a uno, ya que en este caso ya estaria ordenada
        if len(array) <= 1:
            return array
        #seleccionamos un pivote (en este caso el ultimo elemento de la lista) y creamos el conjunto menor al pivote y el mayor al pivote
        pivote = array[-1]
        izquierda = []
        derecha = []
        # exploramos el array de el primer elemento hasta el pivote excluyendo a este
        for i in array[:-1]:
            # si el elemento es menor o igual al pivote lo enviamos a el conjunto izquierdo(menor que pivote)
            if i <= pivote:
                izquierda.append(i)
            # sino mandamos el elemento al conjunto derecho(mayor que el pivote)
            else:
                derecha.append(i)
        # luego llamamos a la funcion recursivamente enviando como parametro los dos arrays creados con los elementos mayores y menores que el pivote
        quick_izquierda = self.quicksort(izquierda)
        quick_derecha = self.quicksort(derecha)
        #despues de que termine cada llamado a la funcion, juntamos el array que dividimos en 3 pero ya acomodado(de izquierda a pivote a derecha)
        return quick_izquierda + [pivote] + quick_derecha

    def pares(self, contador=0):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            dato = actual.dato
            if dato % 2 == 0:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print(f"\nEl {actual.dato} se ha eliminado")
                self.pares(contador+1)
                return
            anterior = actual
            actual = actual.siguiente
        print(f"\nSe eliminaron {contador} numeros pares")
        print(f"\nLa lista queda así:")


def aleatorio():
        numero=0
        for i in range(1000):
            numero=random.randint(1,100)
            lista.agregar_nodo(numero)
            
if __name__ == "__main__":
    lista = ListaEnlazada()
    while True:
        seleccion=int(input("\n¿Que deseas hacer?\n1.-Agregar Nodo\n2.-Buscar Valor\n3.-Eliminar Valor\n4.-Modificar valor\n5.-Mostrar\n6.-Ordenar\n7.-Salir\n8-Pares\n"))
        if seleccion == 1:
            op=int(input("¿Deseas rellenar de 10 numeros aleatorios?\n1.-Si  .-No\n"))
            if op==1:
                aleatorio()
            else:
                lista.agregar_nodo(int(input("Que valor deseas agregar")))
                print("Lista enlazada de un solo enlace: ", end="")
            lista.imprimir_lista()
        elif seleccion ==2:
            lista.buscar_valor(int(input("Que valor deseas buscar")))
        elif seleccion ==3:
            lista.eliminar_valor(int(input("Que valor deseas eliminar")))
        elif seleccion ==4:
            lista.modificar_valor(int(input("Que valor deseas modificar")))
        elif seleccion ==5:
            lista.imprimir_lista()
        elif seleccion ==6:
            lista.acomodar_quicksort()
            print("\nLista enlazada acomodada con Quicksort: ", end="")
            lista.imprimir_lista()
        elif seleccion==7:
            print("\nSaliendo...")
            break
        elif seleccion==8:
            lista.pares()
            lista.imprimir_lista()
            