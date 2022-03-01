from app import *
from LinkedList import LinkedList

listPisos = LinkedList()

def run():
    end = False
    selection = 0

    while not end:
        print("------------Menú------------\n1. Cargar Data\n2. Cargar Instrucciones\n3. Análizar\n4. Reportes5. Salir")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            rute = leerArchivo()
        
            if rute != None:
                lecturaArchivosXml(rute)
            else:
                print("sin Cambios")

        elif selection == 2:
            rute = leerArchivo()
            if rute != None:
                print(rute)
            else:
                print("sin Cambios")
        elif selection == 3:
            print("3")
        elif selection == 4:
            print("3")
        elif selection == 5:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()