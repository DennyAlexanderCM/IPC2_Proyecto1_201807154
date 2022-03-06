from functions import *
from colorama import Fore

def run():
    listPisos = None
    end = False
    selection = 0

    while not end:
        print(Fore.YELLOW + "\n============ Menú ============\n 1. Cargar patrones de piso\n 2. Seleccionar piso y patrón\n 3. Pisos cargados\n 4. Salir")
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
            menuOptionsTile(listPisos)
            
        elif selection == 3:
            #COPIAMOS LA LISTA PARA NO MODIFICAR LA LISTA PRINCIPAL
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