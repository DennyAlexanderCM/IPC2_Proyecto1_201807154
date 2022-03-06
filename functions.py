from ast import pattern
from tkinter import filedialog
from xml.dom import minidom
from LinkedList import LinkedList
from LinkedListPatterns import LinkedListPatterns
from tile import Tile
from Pattern import Pattern
from colorama import Fore
from graphviz import Digraph, Graph


def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(Fore.YELLOW + "Introduce una opción: "))
            correcto=True
        except ValueError:
            print(Fore.RED + '¡Error, introduce un numero entero!')
    return num  

def leerArchivo():
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    if root != "":
        return root
    return None

def menuOptionsTile(listPisos):
    end = False
    while not end:
        print(Fore.YELLOW + "\n========= Seleccionar Piso =========\n"+ Fore.RED +">>>> " + Fore.YELLOW + "Pisos Disponibles:")
        #IMPRIMOS LOS NOMBRES DE LOS PISOS ENUMERADOS
        listPisos.printDates()
        #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        #VERIFICAMOS SI LA OPCION ESTA EN EL RANGO
        if listPisos.length() >= selection and selection > 0:
            #BUSCAMOS EL DATO EN NUESTRA LISTA
            dataA = listPisos.searchDate(selection)
            menuOptionsPattern(dataA)
            #TERMINAMOS EL CICLO REPETITIVO
            end = True
        else:
            print(Fore.RED + "¡Ingrese una opción correcta!") 

def menuOptionsPattern(data):
    end = False
    while not end:
        print(Fore.YELLOW + "\n======= Seleccionar Patrón Inicial =======\nPatrones Disponibles piso: " + data.getNombre())
        #IMPRIMOS LOS NOMBRES DE LOS PISOS ENUMERADOS
        data.getPatrones().printDatesNumerate()
         #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        #VERIFICAMOS SI LA OPCION ESTA EN EL RANGO
        if data.getPatrones().length() >= selection and selection > 0:
            #BUSCAMOS EL DATO EN NUESTRA LISTA objeto piso ---> lista de patrones >>funcion para buscar el patron seleccionado
            patronSelected = data.getPatrones().searchDate(selection)
            menuAction(data, patronSelected)
            #TERMINAMOS EL CICLO REPETITIVO
            end = True
        else:
            print(Fore.RED + "¡Ingrese una opción correcta!") 

def menuAction(data, patternSelected):
    end = False
    while not end:
        print(Fore.YELLOW + "\n========= Seleccionar Acción =========\n 1. Gráfico del Pratrón\n 2. Seleccionar Nuevo Patrón\n 3. Regresar")
        #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        if selection == 1:
            graphPatter(data, patternSelected.getPattern())
        elif selection == 2:
            selectSecondPattern(data, patternSelected)
        elif selection ==3:
            end = True
        else:
            print(Fore.RED + "¡Ingrese una opción correcta!") 
       
def selectSecondPattern(data, patterSelected):
    end = False
    n = 1
    n2 = 0
    while not end:
        correct = False
        aux = data.getPatrones().head
        print(Fore.YELLOW + "\n======= Seleccionar Nuevo Patrón =======\nPatrones Disponibles piso: " + data.getNombre())
        #IMPRIMOS LOS NOMBRES DE LOS PISOS ENUMERADOS
        for i in range(data.getPatrones().length()):
            if aux.data.getCode() == patterSelected.getCode():
                print(str(n)+ ". " + aux.data.getCode()+' (Inicial)')
                aux = aux.next
                n2 += n
                n += 1
                
            else:
                print(str(n)+ ". " + aux.data.getCode())
                aux = aux.next
                n +=1
        
        while not correct:
            selection = pedirNumeroEntero()
            if selection != n2:
                if data.getPatrones().length() >= selection and selection > 0:
                    #BUSCAMOS EL DATO EN NUESTRA LISTA objeto piso ---> lista de patrones >>funcion para buscar el patron seleccionado
                    end = True 
                    correct = True
                else:
                    print(Fore.RED + "¡Ingrese una opción correcta!")
            else:
                print(Fore.RED + "¡Ingrese una opción diferente!")

        """
        data.getPatrones().printDatesNumerate()
         #SOLICITAMOS UNA OPCIÓN
        selection = pedirNumeroEntero()
        #VERIFICAMOS SI LA OPCION ESTA EN EL RANGO
        if data.getPatrones().length() >= selection and selection > 0:
            #BUSCAMOS EL DATO EN NUESTRA LISTA objeto piso ---> lista de patrones >>funcion para buscar el patron seleccionado
            patronSelected = data.getPatrones().searchDate(selection)
            menuAction(data, patronSelected)
            #TERMINAMOS EL CICLO REPETITIVO
            end = True
        else:
            print(Fore.RED + "¡Ingrese una opción correcta!") """

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
                    patterns.append(auxPattern)
            date.setPatrones(patterns)
        listPisos.append(date)
    print(Fore.GREEN + "¡Archivo Cargado Correctamente!")
    return listPisos

def graphPatter(tile, patern):
    position = 0
    txt = ""
    #filas
    R = int(tile.getR())
    #columnas
    C = int(tile.getC())
    s = Digraph('html_table' )
    for i in range(R):
        txt +="<TR>"
        for j in range(C):
            if patern[position] == "W":
                txt+='<TD bgcolor="white" border="2"></TD>'
            else:
                txt += '<TD bgcolor="black" border="2"></TD>'
            position +=1
        txt += "</TR>"

    s.node('tab', label='<<TABLE border="0" cellspacing="2" cellpadding="30">'+txt+'</TABLE>>', shape='box')
    s.render('Graficas/Pisos.gv',format='jpg', view=True)