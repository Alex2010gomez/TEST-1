class Reparacion():
    def __init__(self,orden, cliente, equipo, falla, estado, tecnico,costo_estimado):
        self.orden = orden
        self.cliente = cliente  
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado
    
    def mostrardatos(self):
        print(f"Orden : {self.orden} | Cliente {self.cliente} | ")
        print(f"Equipo {self.equipo} | Falla {self.falla} | Estado {self.estado} | Tecnico {self.tecnico} | Costo Aprox {self.costo_estimado}")
        print("x"*100)

objetos = [
    Reparacion(orden=1, cliente="Juan", equipo="Notebook", falla="No enciende", estado="Pendiente", tecnico="Pedro", costo_estimado=15000),
    Reparacion(orden=2, cliente="Maria", equipo="Celular", falla="Pantalla rota", estado="En proceso", tecnico="Ana", costo_estimado=8000),
    Reparacion(orden=3, cliente="Carlos", equipo="Tablet", falla="Bateria no carga", estado="Finalizado", tecnico="Luis", costo_estimado=5000),
    Reparacion(orden=4, cliente="Laura", equipo="Notebook", falla="Teclado dañado", estado="Pendiente", tecnico="Pedro", costo_estimado=12000),
    Reparacion(orden=5, cliente="Jorge", equipo="Celular", falla="No funciona el micrófono", estado="En proceso", tecnico="Ana", costo_estimado=6000),
    Reparacion(orden=6, cliente="Sofia", equipo="Tablet", falla="Pantalla táctil no responde", estado="Finalizado", tecnico="Luis", costo_estimado=7000),
    Reparacion(orden=7, cliente="Diego", equipo="Notebook", falla="Problema de audio", estado="Pendiente", tecnico="Pedro", costo_estimado=9000),
    Reparacion(orden=8, cliente="Valentina", equipo="Celular", falla="No carga la batería", estado="En proceso", tecnico="Ana", costo_estimado=4000),
    Reparacion(orden=9, cliente="Matias", equipo="Tablet", falla="Problema de conectividad", estado="Finalizado", tecnico="Luis", costo_estimado=3000),
    Reparacion(orden=10, cliente="Camila", equipo="Notebook", falla="Pantalla parpadea", estado="Pendiente", tecnico="Pedro", costo_estimado=11000) 
]

#Crear una función buscar_por_orden(numero) que devuelva una reparación o None.

def buscar_por_orden(numero):
    for i in objetos:
        if i.orden == numero:
            return i
    return None

#Crear una función filtrar_por_estado(estado) que muestre las reparaciones que
#coincidan con el estado solicitado.

def filtrar_por_estado(estado):
    resultados = []
    for i in objetos:
        if i.estado.lower() == estado.lower():
            resultados.append(i)
    
    if not resultados:
        print("Sin coincidencias")
    else:
        for o in resultados:
            o.mostrardatos()

#Crear una función filtrar_por_tecnico(tecnico) que permita consultar todas las
#reparaciones asignadas a una persona.

def filtrar_por_tecnico(tecnico):
    resultados = []
    for i in objetos:
        if i.tecnico == tecnico:
            resultados.append(i)
    
    if not resultados:
        print("Sin resultados")
    else:
        for o in resultados:
            o.mostrardatos()

#Crear una función filtrar_por_costo(limite) que muestre las reparaciones cuyo costo
#estimado sea menor o igual al importe indicado.

def filtrar_por_costo(limite):
    resultados = []
    for i in objetos:
        if limite >= i.costo_estimado:
            resultados.append(i)
    
    if not resultados:
        print("Sin resultados ")
    else:
        for o in resultados:
            o.mostrardatos()
    
#Construir un menú con las opciones: 1) Mostrar todas, 2) Buscar por orden, 3) Filtrar por
#estado, 4) Filtrar por técnico, 5) Filtrar por costo y 6) Salir.

while True:
    print("1. Mostrar todos ")
    print("2. Buscar por número de orden ")
    print("3. Filtrar por estado ")
    print("4. Filtrar por técnico ")
    print("5. Filtrar por costo ")
    print("6. Salir ")

    opcion = int(input("Seleccione una opcion : "))
    if opcion == 1 :
        for x in objetos:
            x.mostrardatos()
    
    elif opcion == 2 :
        numero_orden = int(input("Ingrese el numero de orden : "))
        
        resultado = buscar_por_orden(numero_orden)
        if resultado == None :
            print("Sin resultados ")
        else:
            resultado.mostrardatos()

    elif opcion == 3:
        estadop = str(input("Ingrese el estado a filtrar : "))
        filtrar_por_estado(estadop)

    elif opcion == 4:
        tecnicoop = str (input("Ingrese el nombre del tecnico "))
        filtrar_por_tecnico(tecnicoop)
    
    elif opcion == 5:
        limit = float(input("Ingrese el costo limite : "))
        filtrar_por_costo(limit)
    
    elif opcion == 6 :
        print("Adios ")
        break
    
    else:
        print("Error ")