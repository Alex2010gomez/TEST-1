#El colegio necesita registrar una cantidad específica de alumnos de una sola vez.
#Pregunta al usuario '¿Cuántos alumnos desea registrar?'. Utiliza un bucle for para repetir la
#creación del diccionario esa cantidad de veces y guarda cada registro en una Lista. Al finalizar,
#imprime la lista completa.
listado = []

cantidad = int (input("Ingrese la cantidad de veces que quiere registrar : "))
for i in range(cantidad):
    diccionario = {}
    alumno = str (input("Ingrese el nombre del alumno : "))
    diccionario["nombre"] = alumno
    listado.append(diccionario)

for i in listado:
    print (i) 