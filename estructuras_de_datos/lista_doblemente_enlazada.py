# creamos la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

# creamos la clase de la lista doblemente enlazada
class ListaDobleEnlazada:
    #pero ahora agregamos inicio-cabeza y fin-cola
    def __init__(self):
        #las dos inicializadas en null
        self.cabeza = None
        self.cola = None
    
    def agregar_nodo(self, dato):
        #creamos una instancia(un nodo) con el valor dado anteriormente
        nuevo_nodo = Nodo(dato)
        #verificamos si nuestra lista esta vacia, en este caso iniciamos cabeza-inicio y cola-fin en null los dos apuntando en el mismo lugar
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        
        else:
            #como se agrega uno nuevo quiero que el anterior de el nuevo nodo sea el fin((inicio)nodo1->nodo2->nodo3(fin); nuevonodo[anterior]=nodo3(fin))
            nuevo_nodo.anterior = self.cola
            #ahora el anteriormente fin quiero que en lugar de apuntar a null apunte a el nuevo nodo
            self.cola.siguiente = nuevo_nodo
            # y que ademas ahora el fin apunte a el lugar de el nuevo nodo
            self.cola = nuevo_nodo

    def imprimir_lista(self):
        # nos ubicamos al inicio
        actual = self.cabeza
        #iteramos sobre cada nodo imprimiendolo
        while actual is not None:
            #ahora agregamos <-> para que se vea bonito
            print(actual.dato, "<->", end=" ")
            #nos aseguramos que pasemos al siguiente
            actual = actual.siguiente
        print("None")

    def buscar_valor(self, dato):
        #nos ubicamos en el inicio
        actual = self.cabeza
        #nos aseguramos que no sea null porque en caso contrario el elemento no se encontro en la lista
        while actual is not None:
            #si el campo dato en nuestro nodo actual es igual al elemento que estamos buscando
            if actual.dato == dato:
                #imprimimos que si esta
                print("\nEl elemento si se encuentra en la lista")
                return
            #sino seguimo buscando en el nodo siguiente
            actual = actual.siguiente
        #ya que iteramos por toda la lista y nunca se cumplio la condicion, damos por hecho que no se encuentra en la lista
        print("\nEl elemento no se encuentra en la lista")

    def eliminar_valor(self, dato):
        #ubicacion inicio
        actual = self.cabeza
        #nos aseguramos que no sea null porque en caso contrario el elemento no se encontro en la lista
        while actual is not None:
            #si el campo dato en nuestro nodo actual es igual al elemento que estamos buscando para eliminar
            if actual.dato == dato:
                #pero ademas el nodo anterior al que apunta no es null
                if actual.anterior is not None:
                    #entonces el nodo anterior en su campo siguiente debe apuntar hacia el campo siguiente de el nodo actual: tienes: (|inicio)nodo1->nodo2->nodo3(fin)| quieres eliminar (nodo2) |[actual.anterior.siguiente] es nodo1(en su campo siguiente)->[actual.siguiente]nodo3 
                    actual.anterior.siguiente = actual.siguiente
                else:
                    #sino significa que el anterior de el actual es null por lo tanto estamos en el inicio
                    #asi que modificamos el inicio al campo siguiente de el actual
                    self.cabeza = actual.siguiente
                #ahora verificamos si el campo siguiente no es null
                if actual.siguiente is not None:
                    #sino es null entonces el campo anterior de el siguiente nodo quiero que apunte a el anterior de el nodo actual
                    actual.siguiente.anterior = actual.anterior
                #si el siguiente si es null significa que estamos en el fin
                else:
                    #entonces quiero que el fin ahora apunte el nodo anterior
                    self.cola = actual.anterior
                print("\nEl elemento se ha eliminado")
                return
            #si aun no es el elemento que queremos eliminar entonces pasamos al siguiente nodo
            actual = actual.siguiente
        #si todo lo anterior se descarto, significa que el elemento no esta en la lista
        print("\nEl elemento no se encuentra en la lista")

    def modificar_valor(self, dato):
        #inicio
        actual = self.cabeza
        #exploramos toda la lista excepto si es null porque abremos terminado
        while actual is not None:
            #si el campo dato en el nodo actual es igual al dato que queremos modificar 
            if actual.dato == dato:
                #pedimos el nuevo dato
                modificacion = int(input("Ingresa el nuevo valor: "))
                #modificamos el campo dato de el nodo actual por el nuevo valor
                actual.dato = modificacion
                #imprimimos el cambio
                print(f"\nEl número {dato} se ha modificado por el {modificacion}")
                #regresamos para que no sea necesario seguir explorando
                return
            #sino pasamos a siguiente nodo y repetimos
            actual = actual.siguiente
        #si nada de lo anterior funciono damos por hecho que el elemento no se encuentra en la lista
        print("\nEl elemento no se encuentra en la lista")

    #esto es lo mismo de el anterior codigo||
    def acomodar_quicksort(self):
        lista = []
        actual = self.cabeza
        while actual is not None:
            lista.append(actual.dato)
            actual = actual.siguiente
        
        lista = self.quicksort(lista)
        
        self.cabeza = None
        self.cola = None
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

if __name__ == "__main__":
    lista = ListaDobleEnlazada()
    while True:
        seleccion = int(input("\n¿Qué deseas hacer?\n1.-Agregar Nodo\n2.-Buscar Valor\n3.-Eliminar Valor\n4.-Modificar valor\n5.-Mostrar\n6.-Ordenar\n7.-Salir\n"))
        if seleccion == 1:
            lista.agregar_nodo(int(input("Qué valor deseas agregar: ")))
            print("Lista doblemente enlazada: ", end="")
            lista.imprimir_lista()
        elif seleccion == 2:
            lista.buscar_valor(int(input("Qué valor deseas buscar: ")))
        elif seleccion == 3:
            lista.eliminar_valor(int(input("Qué valor deseas eliminar: ")))
        elif seleccion == 4:
            lista.modificar_valor(int(input("Qué valor deseas modificar: ")))
        elif seleccion == 5:
            lista.imprimir_lista()
        elif seleccion == 6:
            lista.acomodar_quicksort()
            print("\nLista acomodada con Quicksort: ", end="")
            lista.imprimir_lista()
        elif seleccion == 7:
            print("\nSaliendo...")
            break
