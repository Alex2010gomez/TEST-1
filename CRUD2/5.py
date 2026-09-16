
diccionario = {}
def registrar_N_alumno():
    nombre = str (input("Ingrese el nombre del alumno : "))
    try :
        edad = int (input("Ingrese la edad del alumno : "))
        dni = int (input ("Ingrese el dni del alumno "))
    except ValueError:
        print("Ingrese el DNI y la Edad en numeros ")
    
    try:
        with open("alumnos.txt","a" , encoding="utf-8") as documento :
            documento.write(f"Nombre: {nombre} Edad {edad}  DNI {dni} ")
        
    except ValueError:
        print("Error al cargar los datos al .txt")    
        
registrar_N_alumno()