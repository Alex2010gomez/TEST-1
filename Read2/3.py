lista_alumnos = [ #Lista con datos de alumnos almacenados en diccionarios 
    {"nombre": "Ana García","curso": "5to A","promedio": 8.5,"tp_entregados": 12},
    {"nombre": "Bruno López","curso": "5to B","promedio": 6.2,"tp_entregados": 9},
    {"nombre": "Clara Martínez","curso": "5to A","promedio": 9.7,"tp_entregados": 12},
    {"nombre": "Daniel Rodríguez","curso": "6to A","promedio": 4.5,"tp_entregados": 7},
    {"nombre": "Elena Gómez","curso": "6to B","promedio": 7.8,"tp_entregados": 11},
    {"nombre": "Facundo Fernández","curso": "5to B","promedio": 5.9,"tp_entregados": 8},
    {"nombre": "Gabriela Pérez","curso": "6to A","promedio": 8.9,"tp_entregados": 12},
    {"nombre": "Hugo Sánchez","curso": "5to A","promedio": 7.1,"tp_entregados": 10},
    {"nombre": "Irene Díaz","curso": "6to B","promedio": 9.2,"tp_entregados": 12},
    {"nombre": "Juan Romero","curso": "6to A","promedio": 3.8,"tp_entregados": 5}
]

prom = float(input("Ingrese el promedio solo con numeros : "))
minimo = int(input("Ingrese la cantidad minima de trabajos : "))

filtrado = []
cumple = 0
nocumple = 0
promediomax = None #Tiene que estar si o si en NONE y no con una lista vacia para que al evaluar su contenido python no lo ignore por estar vacio 

for i in lista_alumnos: #Recorre la lista 
    if i["promedio"] >= prom and i["tp_entregados"] >= minimo: #Si el promedio es mayor a lo ingreso y la cantidad de tp es mayor a la ingresada 
        filtrado.append(i)
        cumple += 1 #Contador , que tambien se podria usar un len pero no recuerdo porque lo hice haci 
    else:
        nocumple += 1 
    if promediomax is None or i["promedio"] > promediomax["promedio"]: #Si promedio max es None o el resultado es mayor a lo guardado en la lista 
        promediomax = i

print(f"Alumnos que cumplen: {cumple}")
print(f"Alumnos que no cumplen: {nocumple}")
print("El alumno con el promedio más alto de la lista es:")
print(promediomax)
for u in filtrado:
    print(u)
