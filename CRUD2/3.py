
listado = []

cantidad = int (input("Ingrese la cantidad de veces que quiere registrar : "))
for i in range(cantidad):
    diccionario = {}
    alumno = str (input("Ingrese el nombre del alumno : "))
    edad = int (input("Ingrese la edad del alumno : "))
    if edad > 17 and 99 > edad : 
        diccionario["nombre"] = alumno
        listado.append(diccionario)
        print("Agregado correctamente ")
    else : 
        print("La edad esta fuera del rango permitido ")

for i in listado:
    print (i) 