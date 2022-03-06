from colorama import Fore
#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#CLASE DE LA LISTA ENLAZADA DE LOS PISOS
class LinkedList:
    def __init__(self):
        self.name = None
        self.head = None
        self.last = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(selft):
        return selft.head

    #AGREGAMOS LOS DATOS AL INICIO
    def add(selft , data):
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

    #IMPRIMIMOS LOS DATOS DE LA LISTA
    def printDates(selft):
        i = selft.head
        n = 1
        while i:
            print(str(n)+". "+i.data.getNombre())
            i = i.next
            n+=1

    #COPIAMOS LA LISTA
    def copyList(selft):
        i = selft.head
        listAux = LinkedList()
        while i:
            listAux.add(i.data)
            i = i.next
        return listAux
        
    #RETORNAR EL NÚMERO DE ELEMENTOS
    def length(selft):
        n = 0
        i = selft.head
        while i:
            i = i.next
            n+=1
        return n

    #ORDEAMOS ALFABETICAMNTE POR EL NOMBRE
    def sortList(self):
        end = None
        while end != self.head:
            aux = self.head
            while aux .next != end:
                q = aux .next
                if aux.data.getNombre() > q.data.getNombre():
                    aux.data, q.data = q.data, aux.data
                aux = aux.next
            end = aux
    
    #ORDEAMOS ALFABETICAMNTE POR EL NOMBRE LOS PATRONES
    def sortListPatterns(selft):
        i = selft.head
        while i:
            i.data.getPatrones().sortList()
            i = i.next

    #IMPRIMIMOS LOS PATRONES
    def printPaterns(selft):
        i = selft.head
        while i:
            i.data.getPatrones().printDates()
            i = i.next

     #BUSCAMOS UN DATO EN ESPECIFICO -->nombre
    def searchDate(selft, data):
        i = selft.head
        while i:
            if i.data.getName() == data:
                return i
            else:
                i = i.next
        return False

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

    #IMPRIMIMOS TODOS LOS DATOS DE LOS PISOS
    def printAllDates(selft):
        i = selft.head
        print(Fore.RED + "\n\n>>>>" + Fore.YELLOW +"Pisos cargados al sistema:")
        while i:
            print(Fore.YELLOW + "\nNombre:", i.data.getNombre())
            i.data.getPatrones().printDates()
            i = i.next
            

    #COLOCAR EL ELEMENTO NOMBRE
    def setName(selft, name):
        selft.name = name
    

