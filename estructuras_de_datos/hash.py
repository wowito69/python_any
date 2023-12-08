import random
class Nodo_campo_usuario:
    def __init__(self, id,dato):
        self.id = id
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Nodo_lista_enlace:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.abajo=None
        
class ListaHash:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_nodo(self, dato):
        #creamos un objeto nodo
        nuevo_nodo = Nodo_lista_enlace(dato)
        #si el primer nodo esta vacio
        if self.cabeza is None:
            #inicio es igual al nuevo nodo
            self.cabeza = nuevo_nodo
            #fin es igual al nuevo nodo
            self.cola = nuevo_nodo
        else:
            #el campo anterior de el nuevo nodo apunta a la cola-fin
            nuevo_nodo.anterior = self.cola
            #luego el siguiente de la cola-fin apunta al nuevo para que esten doblemente enlazados
            self.cola.siguiente = nuevo_nodo
            #y otorgamos el fin a el nuevo nodo
            self.cola = nuevo_nodo

    def agregar_nodo_usuario(self,id, dato):
        #creamos un objeto nodo
        nuevo_nodo = Nodo_campo_usuario(id,dato)
        #si el primer nodo esta vacio
        if self.cabeza is None:
            #inicio es igual al nuevo nodo
            self.cabeza = nuevo_nodo
            #fin es igual al nuevo nodo
            self.cola = nuevo_nodo
        else:
            #el campo anterior de el nuevo nodo apunta a la cola-fin
            nuevo_nodo.anterior = self.cola
            #luego el siguiente de la cola-fin apunta al nuevo para que esten doblemente enlazados
            self.cola.siguiente = nuevo_nodo
            #y otorgamos el fin a el nuevo nodo
            self.cola = nuevo_nodo
    def imprimir_lista(self):
            #nos colocamos en el nodo del inicio
            actual = self.cabeza
            #vamos nodo por nodo imprimiendo
            while actual is not None:
                print(actual.dato, "<->", end=" ")
                actual = actual.siguiente
            #nuestro final de la lista nunca esta indicado pero sabemos que siempre apunta a null-none
            print("None")
    def imprimir_lista_hash(self):
            #nos colocamos en el nodo del inicio
            actual = self.cabeza
            #vamos nodo por nodo imprimiendo
            while actual is not None:
                print(actual.id,actual.dato, "<->", end=" ")
                actual = actual.siguiente
            #nuestro final de la lista nunca esta indicado pero sabemos que siempre apunta a null-none
            print("None")

    def buscar_valor(self, dato):
        actual = self.cabeza
        #aqui no funciona la condicion "is not none" porque en una lista circular nunca se va apuntar a null
        while True:
            #en esta condicion buscamos datos por dato y si es lo imprimimos y regresamos
            if actual.dato == dato:
                print("\nEl elemento se encuentra en la lista")
                return
            #nos aseguramos de pasar al siguiente y si el siguiente es el inicio significa que ya la recorrimos y no se encontro
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("\nEl elemento no se encuentra en la lista")


    def eliminar_valor(self, dato):
    #nos ubicamos al inicio de la lista
        actual = self.cabeza
        # recorremos la lista en un bucle mientras el nodo actual no sea nulo
        while actual is not None:
            # cerificamos si el valor en el nodo actual es igual al valor que deseamos eliminar
            if actual.dato == dato:
                # comprobamos si el nodo actual tiene un nodo anterior (no es el primer nodo)
                if actual.anterior is not None:
                    # ajusto los punteros del nodo anterior para omitir el nodo actual entonces el anterior en su campo siguiente apunta a el nodo siguiente de el actual
                    actual.anterior.siguiente = actual.siguiente
                    # ajusto los punteros del nodo siguiente para omitir el nodo actual entonces el siguiente en su campo anterior apunta al nodo anterior de el actual
                    actual.siguiente.anterior = actual.anterior
                    # comprobamos si el nodo actual es la cabeza de la lista
                    if actual == self.cabeza:
                        # si es la cabeza, actualizamos la cabeza para que apunte al siguiente nodo
                        self.cabeza = actual.siguiente
                    # comprobamos si el nodo actual es la cola de la lista
                    if actual == self.cola:
                        # si es la cola, actualizamos la cola para que apunte al nodo anterior
                        self.cola = actual.anterior
                # imprimimos un mensaje para indicar que el elemento se ha eliminado con éxito
                print("\nEl elemento se ha eliminado")
                # regresamos de la función porque ya hemos realizado la eliminación
                return
            # si el nodo actual no contiene el valor deseado, avanzamos al siguiente nodo
            actual = actual.siguiente
        # si el bucle completa su recorrido y no encuentra el valor deseado, imprimimos un mensaje indicando que no se encontró
        print("\nEl elemento no se encuentra en la lista")


    def modificar_valor(self, dato):
        #esto es lo mismo que los otros
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                modificacion = int(input("Ingresa el nuevo valor: "))
                actual.dato = modificacion
                print(f"\nEl número {dato} se ha modificado por el {modificacion}")
                return
            actual = actual.siguiente
        print("\nEl elemento no se encuentra en la lista")

    def hash_1(self,id,nombre):
        actual=self.cabeza
        hash=id%100
        while actual is not None:
            if actual.dato==hash:
                if actual.abajo is None:
                    lista_abajo=ListaHash()
                    lista_abajo.agregar_nodo_usuario(id,nombre)
                    actual.abajo=lista_abajo.cabeza
                    actual=actual.siguiente
                else:
                    lista_abajo.agregar_nodo_usuario(id,nombre)
                    actual=actual.siguiente
            else:
                actual=actual.siguiente
        lista_abajo.imprimir_lista_hash()
        
if __name__=="__main__":
    while True:
        opc=int(input("Bienvenido\n¿Quieres registrarte?\n1.-Si\n2.-No\n3.-Salir"))
        if opc==1:
            Lista_base=ListaHash()
            for i in range(0,100):
                Lista_base.agregar_nodo(i)
            id=(random.randint(4000,6000))**2
            nombre=input("Ingresa tu nombre de usuario")
            print(f"Bienvenido Usuario {nombre}, tu ID es: {id}")
            Lista_base.hash_1(id,nombre)
        elif opc==3: break