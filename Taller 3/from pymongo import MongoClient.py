"""Para instalar MongoDB y PyMongo, primero debes asegurarte de que tu sistema cumple con los requisitos 
necesarios. En Windows, puedes descargar el instalador MSI desde la página oficial de MongoDB, ejecutarlo 
y seguir las instrucciones, asegurándote de habilitar la opción para ejecutarlo como un servicio si quieres 
que se inicie automáticamente. Luego, puedes verificar la instalación abriendo una terminal y ejecutando 
mongod --version. Si MongoDB no se ejecuta automáticamente, puedes iniciarlo manualmente con mongod en una 
terminal y luego abrir otra para ejecutar mongo y acceder a la base de datos.""""" 

"""Para instalar PyMongo, la biblioteca de Python para conectarse con MongoDB, simplemente ejecuta pip  "
"install pymongo en la terminal. Para comprobar que se instaló correctamente, abre Python e importa PyMongo  "
"con import pymongo, luego imprime su versión con print(pymongo.__version__). Si todo funciona sin errores, "
"significa que la instalación fue exitosa. """

from pymongo import MongoClient
import sys 

Mongo_URI = "mongodb://localhost" 
client = MongoClient(Mongo_URI) 
db = client["Libreria"] 
collection = db["Libros"] 
 

class Libro: 
    def __init__(self,titulo,genero,autor,estado): 
        self.titulo = titulo 
        self.genero = genero 
        self.autor = autor 
        self.estado = estado
        

def agregar_libro(): 
    try:
        titulo = input("Titulo del libro: ")  
        genero = input("Genero del libro: ")  
        autor = input("Nombre del autor: ")  
        estado = input("Estado del libro: ")

        nuevo_libro = Libro(titulo=titulo, genero=genero, autor=autor, estado=estado) 
        collection.insert_one({"titulo": nuevo_libro.titulo,"genero": nuevo_libro.genero,"autor": nuevo_libro.autor,"estado": nuevo_libro.estado})
         

        print("Libro agregado exitosamente.") 
    except Exception as c:  
        print("Error al agregar libro {c}" )     

def actualizar_libro(): 
    try:
        titulo_buscar = input("Ingrese el título del libro que quiere modificar: ")
        
    
        """if libro is None:
            print("El libro no existe")
            return"""
    
        print("1.Actualizar titulo")       
        print("2.Actualizar autor")       
        print("3.Actualizar genero")       
        print("4.Actualizar estado\n")       
        w = int(input("Elija una opcion: ")) 

        if w == 1: 
            busqueda = input("Escriba el nuevo titulo del libro: ") 
            collection.update_one({"titulo": titulo_buscar}, {"$set": {"titulo": busqueda}}) 
        elif w == 2: 
            busqueda = input("Escriba el nuevo autor del libro: ") 
            collection.update_one({"titulo": titulo_buscar}, {"$set": {"autor": busqueda}}) 
        elif w == 3: 
            busqueda = input("Escriba el nuevo genero del libro: ") 
            collection.update_one({"titulo": titulo_buscar}, {"$set": {"genero": busqueda}}) 
        elif w == 4: 
            busqueda = input("Escriba el nuevo estado del libro: ") 
            collection.update_one({"titulo": titulo_buscar}, {"$set": {"estado": busqueda}}) 
            
         
    except Exception as c:  
        print("Error al actualizar el libro {c}")        

def eliminar_libro(): 
    try:
        titulo_buscar = input("Ingrese el titulo del libro que desea eliminar de la base de datos: ")   
        collection.delete_one({"titulo": titulo_buscar}) 

        print("Libro eliminado")
    except Exception as c:  
        print("Error al eliminar el libro {c}")
     
def ver_libros(): 
    try:  
        listado = collection.find() 

        for i in listado: 
            print(i) 
    except Exception as c:  
        print("Error al mostar libros {c}")

def buscar_libro(): 
    try:
        print("1.Buscar por titulo")       
        print("2.Buscar por autor")       
        print("3.Buscar por genero\n")       
        w = int(input("Elija una opcion: ")) 

        if w == 1: 
            busqueda = input("Escriba el titulo del libro: ") 
            libro = collection.find({"titulo": busqueda})
        elif w == 2: 
            busqueda = input("Escriba el autor del libro: ") 
            libro = collection.find({"autor": busqueda})
        elif w == 3: 
            busqueda = input("Escriba el genero del libro: ") 
            libro = collection.find({"genero": busqueda})

        for i in libro: 
            print(i)     
    except Exception as c:  
        print("Error al buscar libro {c}") 
  
while True: 
    print("1.Ingresar libro")
    print("2.Actualizar informacion del libro")
    print("3.Eliminar libro")
    print("4.Ver libros")  
    print("5.Buscar libros")
    print("6.Salir") 
    e = int(input("Elija una opcion: ")) 

    if e == 1: 
        agregar_libro() 
    
    elif e == 2:
        actualizar_libro() 

    elif e == 3: 
        eliminar_libro()     

    elif e == 4: 
        ver_libros()               

    elif e == 5:
        buscar_libro() 

    elif e == 6:                   
      break 

    else: 
        print("Opcion no valida")




 