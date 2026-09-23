# Clase principal 
class gestoracademico ():
    def __init__(self):
        self.__base_datos_alumnos = []
    
    @property #Metodo para ver la lista 
    def getlista(self):
        for i in self.__base_datos_alumnos:
            print (i)
    
    def agregaralumno (self): #Metodo para guardar los datos pero solo se guardan temporalmente 
        nombre = str (input("Ingrese el nombre del alumno : "))
        dni = int (input("Ingrese el dni del alumno : "))
        alumno = {"nombre":nombre , "dni":dni}
        comprobacion = {alumno["dni"] for alumno in self.__base_datos_alumnos} #Se clonan los datos de la lista para luego compararlos
        
        if alumno["dni"] not in comprobacion:# Si el DNI almacenado en alumno no esta en comprobacion permite que se guarde
            self.__base_datos_alumnos.append(alumno) 
            print("Agregado correctamente")
        else : 
            print("Ocurrio un error o el DNI ya esta cargado ")
test = gestoracademico() #Creacion del objeto
while True:
    print("1. Agregar alumno")
    print("2. Ver registro")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion : "))
    if opcion == 1 :
        test.agregaralumno()
    elif opcion == 2 :
        test.getlista
    elif opcion == 3 :
        print("Adios")
        break
    else : 
        print("Error")
    