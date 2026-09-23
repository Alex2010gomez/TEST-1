#clase base 
class Guardardatos:
    def guardado(self, datos):
        pass

class GuardadoTemporal(Guardardatos):
    def __init__(self):
        self.__datos_alumnos = [] 

    def guardado(self, datos):
        self.__datos_alumnos.append(datos)

    @property #metodo para poder acceder a los datos 
    def getlista(self):
        return self.__datos_alumnos

class GuardadoPerma(Guardardatos):
    def guardado(self, datos):
        with open("alumnos.txt", "a", encoding="utf-8") as documento:
            documento.write(f"{datos}")

almacen_temp = GuardadoTemporal()
almacen_perma = GuardadoPerma()

class GestorAcademico: #Clase principal 
    def __init__(self):
        self.almacen = almacen_temp

    def agregaralumno(self):
        nombre = str(input("Ingrese el nombre del alumno: "))
        dni = int(input("Ingrese el dni del alumno: "))
        alumno = {"nombre": nombre, "dni": dni}
        
        lista_actual = self.almacen.getlista
        comprobacion = {al["dni"] for al in lista_actual} #Clona los datos de la lista para poder compararlos luego
        
        if alumno["dni"] not in comprobacion: #Compara los datos clonados 
            # Guardado en memoria temporal 
            self.almacen.guardado(alumno)
            # Guardado en txt 
            almacen_perma.guardado(alumno)
            print("Agregado correctamente\n")
        else:
            print("Ocurrio un error o el DNI ya esta cargado")

    def mostrar_registro(self):
        lista = self.almacen.getlista
        if not lista:
            print("No hay alumnos registrados")
        else:
            for al in lista:
                print(f"Nombre: {al['nombre']} | DNI: {al['dni']}")

# Bucle principal
test = GestorAcademico()
while True:
    print("1. Agregar alumno")
    print("2. Ver registro")
    print("3. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            test.agregaralumno()
        elif opcion == 2:
            test.mostrar_registro()
        elif opcion == 3:
            print("Adios")
            break
        else:
            print("Opción inválida.")
    except ValueError:
        print("Por favor, ingrese un número válido.")