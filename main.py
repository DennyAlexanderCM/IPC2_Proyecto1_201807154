from tkinter import *
from tkinter import filedialog

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num 

def leerArchivo():
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Data","*.data"),("Todos los archivos","*.*")))
    if root != "":
        file = open(root,'r')
        contentFile = file.read()
        return contentFile
    return None

def run():
    end = False
    selection = 0
    while not end:
        print("------------Menú------------")
        print("1. Cargar Data\n2. Cargar Instrucciones\n3. Análizar\n4. Reportes\n5. Salir")
        selection = pedirNumeroEntero()

        if selection == 1:
            rute = leerArchivo()
            if rute != None:
                print(rute)
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

if __name__ == '__main__':
    run()