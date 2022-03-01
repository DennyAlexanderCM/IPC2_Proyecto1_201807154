class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.name = None
        self.head = None
        self.last = None

    def emply(selft):
        return selft.head

    #agregar al inicio
    def add(selft , data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
            selft.last = nodo
        else:
            nodo.next = selft.head
            selft.head = nodo
    
    #agrega al final de la cola
    def append(selft, data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
        else:
            selft.last.next = nodo
            selft.last = nodo

    #imprimir lista enlazada
    def printDates(selft):
        i = selft.head
        while i:
            print(i.data)
            i = i.next
    #retornar el tamaño de la lista
    def length(selft):
        n = 0
        i = selft.head
        while i:
            i = i.next
            n+=1
        return n

    def searchDate(selft, data):
        i = selft.head
        while i:
            if i.data == data:
                return True
            else:
                i = i.next
        return False

    def invertList(selft):
        prev = sig = None
        i = selft.head
        while i:
            sig = i.next
            i.next = prev
            prev = i
            i = sig
        selft.head = prev 

    def setName(selft, name):
        selft.name = name

if __name__ == "__main__":
        li = LinkedList()
        li.add(2)
        li.add(3)
        li.add(8)
        li.add(9)
        li.append(4)
        li.append(5)
        li.printDates()
        print(li.length())
        li.invertList()
        li.printDates()
