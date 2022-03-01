from app import *
from LinkedList import LinkedList
from tile import Tile

def run():
    listPisos = None
    end = False
    selection = 0

    while not end:
        print("\n-------------Menú-------------\n1. Cargar patrones de piso\n2. Seleccionar piso y patrón\n3. Pisos cargados\n4. Salir")
        selection = pedirNumeroEntero()
        
        if selection == 1:
            #OBTENEMOS LA RUTA DEL ARCHIVO
            rute = leerArchivo()
            #VERIFICAMOS SI LA RUTA NO ESTA VACÍA
            if rute != None:
                listPisos = lecturaArchivosXml(rute)
            else:
                print("sin Cambios")

        elif selection == 2:
            #SUB MENÚ
            menuOptions(listPisos)
        elif selection == 3:
            #COPIAMOS LA LISTA
            copyOfList = listPisos.copyList()
            #ORDENAMOS LA LISTA POR EL NOMBRE DEL PISO
            copyOfList.sortList()
            #ORDENAMOS LA LISTA POR EL NOMBRE DEL CODIGO DEL PATRON DE CADA PISO
            copyOfList.sortListPatterns()
            copyOfList.printAllDates()
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()