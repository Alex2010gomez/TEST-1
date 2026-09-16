lista = [
    {"Nombre":"More" ,"dni": 5017}
]

while True : 
    Nombre = str (input("Ingrese el nombre del alumno ")).lower()
    if Nombre == 'salir':
        print ("Adios")
        break
    dni = int (input("Ingrese el dni del alumno "))
    
    nuevo_alumno = {"Nombre":Nombre,"dni":dni}
    
    comprobacion = {alumno["dni"] for alumno in lista}
    
    if nuevo_alumno["dni"] not in comprobacion : 
        lista.append(nuevo_alumno)
        print("Agregado correctamente ")
    elif nuevo_alumno["dni"] in comprobacion:
        print("El dni ya esta registrado ")
    else:
        print("error ")