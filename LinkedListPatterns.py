from colorama import Fore
#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#CLASE DE LA LISTA ENLAZADA PARA GUARGAR LOS PATRONES DE CADA PISO
class LinkedListPatterns:
    def __init__(self):
        self.head = None
        self.last = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(selft):
        return selft.head

    #AGREGAMOS LOS DATOS AL INICIO
    def add(selft, data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
            selft.last = nodo
        else:
            nodo.next = selft.head
            selft.head = nodo
    
    #AGREGAMOS LOS DATOS AL FINAL
    def append(selft, data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
            selft.last = nodo
        else:
            selft.last.next = nodo
            selft.last = nodo

    #COPIAMOS LA LISTA
    def copyList(selft):
        i = selft.head
        listAux = LinkedListPatterns()
        while i:
            listAux.add(i.data)
            i = i.next
        return listAux
    
    #ORDEAMOS ALFABETICAMNTE POR EL NOMBRE USANDO BUBBLE SORT
    def sortList(self):
        end = None
        while end != self.head:
            aux = self.head
            while aux.next != end:
                q = aux.next
                if aux.data.getCode() > q.data.getCode():
                    aux.data, q.data = q.data, aux.data
                aux = aux.next
            end = aux
    
    #IMPRIMIMOS LOS DATOS DE LA LISTA
    def printDates(selft):
        i = selft.head
        while i:
            print("  Código: "+i.data.getCode())
            print("   Patrón: " + i.data.getPattern())
            i = i.next
    
    #RETORNAR EL NÚMERO DE ELEMENTOS
    def length(selft):
        n = 0
        i = selft.head
        while i:
            i = i.next
            n+=1
        return n

    def printDatesNumerate(selft):
        i = selft.head
        n = 1
        while i:
            print(str(n) +". "+ i.data.getCode())
            print(Fore.LIGHTBLUE_EX + "  Patrón: " +Fore.YELLOW+ i.data.getPattern())
            i = i.next
            n +=1
    #BUSCAMOS UN DATO EN ESPECIFICO POR SU POSICION
    def searchDate(selft, selection):
        n = 1
        i = selft.head
        while i:
            if selection == n:
                return i.data
            else:
                n +=1 
                i = i.next
        return False