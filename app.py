from tkinter import filedialog
from xml.dom import minidom
from LinkedList import LinkedList
from LinkedListPatterns import LinkedListPatterns
from tile import Tile
from Pattern import Pattern

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num 

def leerArchivo():
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    
    if root != "":
        return root
    return None

def menuOptions(listPisos):
    end = False
    while not end:
        print("\n--------Seleccionar Piso--------\nPisos Disponibles:")
        #IMPRIMOS LOS NOMBRES DE LOS PISOS ENUMERADOS
        listPisos.printDates()
        #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        #VERIFICAMOS SI LA OPCION ESTA EN EL RANGO
        if listPisos.length() >= selection:
            #BUSCAMOS EL DATO EN NUESTRA LISTA
            dateA = listPisos.searchDate(selection)
            menuSubOptions(dateA)
            #TERMINAMOS EL CICLO REPETITIVO
            end = True
        else:
            print("Intente de Nuevo")

def menuSubOptions(date):
    end = False
    while not end:
        print("\n------Seleccionar Patrón------\nPatrones Disponibles para el piso: " + date.getNombre())
        #IMPRIMOS LOS NOMBRES DE LOS PISOS ENUMERADOS
        date.getPatrones().printDatesNumerate()
         #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        #VERIFICAMOS SI LA OPCION ESTA EN EL RANGO
        if date.getPatrones().length() >= selection:
            #BUSCAMOS EL DATO EN NUESTRA LISTA objeto piso ---> lista de patrones >>funcion para buscar el patron seleccionado
            dateA = date.getPatrones().searchDate(selection)
            print(dateA.getCode())
            #TERMINAMOS EL CICLO REPETITIVO
            end = True
        else:
            print("Intente de Nuevo")


def lecturaArchivosXml (data):
    listPisos = LinkedList()
    doc = minidom.parse(data)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    listPisos.setName(rootNode.nodeName)
    # Todos los pisos
    pisos = rootNode.getElementsByTagName("piso")
    
    #recorremos los pisos disponibles
    for piso in pisos:
        #creamos el objeto piso
        date = Tile()
        if piso.hasAttribute("nombre"):
            patterns = LinkedListPatterns()
            nombre = piso.getAttribute("nombre")
            r = piso.getElementsByTagName("R")[0].firstChild.data
            c = piso.getElementsByTagName("C")[0].firstChild.data
            f = piso.getElementsByTagName("F")[0].firstChild.data
            s = piso.getElementsByTagName("S")[0].firstChild.data
            date.setNombre(nombre)
            date.setR(r)
            date.setC(c)
            date.setF(f)
            date.setS(s)
            
            #print(date.getNombre(), date.getR(), date.getC(), date.getF(), date.getS())
            datesOfPatterns = piso.getElementsByTagName("patrones")
            patrones = datesOfPatterns[0].getElementsByTagName("patron")
            for pattern in patrones:
                if pattern.hasAttribute("codigo"):
                    auxPattern = Pattern()
                    code = pattern.getAttribute("codigo")
                    codePatter = pattern.firstChild.data.strip()
                    auxPattern.setCode(code)
                    auxPattern.setPattern(codePatter)
                    patterns.add(auxPattern)
            date.setPatrones(patterns)
        listPisos.add(date)
    print("Con éxito")
    return listPisos