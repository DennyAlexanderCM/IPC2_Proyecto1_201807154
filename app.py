from tkinter import filedialog
from xml.dom import minidom
from LinkedList import LinkedList
from tile import Tile

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
    #obtenemos la direccion local del archivo
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    
    if root != "":
        return root
    return None

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
            
            print(date.getNombre(), date.getR(), date.getC(), date.getF(), date.getS())
            
            """#patrones = piso.getElementsByTagName("patrones")
            patron = piso.getElementsByTagName("patrones")
            patrones = patron[0].getElementsByTagName("patron")
           for i in patrones:
                if i.hasAttribute("codigo"):
                    print("Nombre Patrones: ",i.getAttribute("codigo"))"""
        listPisos.add(date)
    
    return listPisos