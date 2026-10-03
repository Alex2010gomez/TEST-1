ordenes_reparacion = [ # lista de objetos , tengo que dejar de generarlas con ia son mas los problemas que me dan estos diccionarios que el tiempo que ahorran 
    {"numero_orden": 1,"cliente": "Juan Pérez","equipo": "Notebook Asus ZenBook","falla": "No enciende, posible pin de carga","estado": "En diagnostico","costo_estimado": 45000.00},
    {"numero_orden": 2,"cliente": "María González","equipo": "iPhone 13 Pro","falla": "Pantalla rota por caída","estado": "Esperando repuesto","costo_estimado": 120000.00},
    {"numero_orden": 3,"cliente": "Carlos Rodríguez","equipo": "Impresora HP Laserjet","falla": "Atasco de papel constante","estado": "En reparacion","costo_estimado": 25000.00},
    {"numero_orden": 4,"cliente": "Ana Martínez","equipo": "PlayStation 5","falla": "Sobrecalentamiento y apagado","estado": "Listo para retirar","costo_estimado": 35000.00},
    {"numero_orden": 5,"cliente": "Luis Gómez","equipo": "PC de Escritorio","falla": "Pantallazo azul (BSOD) aleatorio","estado": "En diagnostico","costo_estimado": 18000.00},
    {"numero_orden": 6,"cliente": "Laura Fernández","equipo": "MacBook Air M1","falla": "Teclado no responde (derrame de líquido)","estado": "Presupuestado","costo_estimado": 95000.00},
    {"numero_orden": 7,"cliente": "Pedro Sánchez","equipo": "Smart TV Samsung 55\"","falla": "Tiene audio pero no da imagen","estado": "En reparacion","costo_estimado": 60000.00},
    {"numero_orden": 8,"cliente": "Sofía Romero","equipo": "Tablet Lenovo P11","falla": "No conecta a redes Wi-Fi","estado": "Listo para retirar","costo_estimado": 15000.00}
]


def buscar_orden(numero): #Funcion para buscar por numero de orden 
    filtrado_numero = [] #Lista para guardar posibles resultados correctos
    for i in ordenes_reparacion:
        if i["numero_orden"] == numero: # Si el numero de orden tiene alguna coincidencia 
            filtrado_numero.append(i) 
    if not filtrado_numero: #si la lista esta vacia 
        print("Orden no encontrada ")
    else:#Si no 
        for e in filtrado_numero:
            print(e)


def filtrar_estado(estado): # Funcion para filtrar por estado del dispositvo 
    resultados = [] #Lista para almacenar resultados 
    for i in ordenes_reparacion: 
        if estado.lower() in i["estado"].lower(): #Si el estado en minuscular coincide con un estado almacenado pasado a minuscula
            resultados.append(i)
            
    if not resultados:
        print("No hay ordenes en este estado ")
    else:
        for e in resultados:
            print(e)

def filtrar_costo(limite): #Filtrar por limite 
    resultado = []
    for i in ordenes_reparacion:
        if limite >= i["costo_estimado"]:
            resultado.append(i)
    if not resultado:
        print(" No hay ordenes menores a este presupuesto")
    else:
        for e in resultado:
            print(e)
            
            
while True: #Bucle de control 
    print("1. Buscar por numero de la orden ")
    print("2. Buscar por estado (no es necesario que escriba el estado completo)")
    print("3. Buscar por limite de costo")
    print("4. Mostrar todas las ordenes")
    print("5. Salir")
    opcion = int(input("Seleccione una opcion "))
    if opcion == 1 :
        ordennumero = int (input("Ingrese el numero de orden"))
        buscar_orden(ordennumero)
    elif opcion == 2 :
        ordenestado = str(input("Ingrese el estado (no es necesario que lo escriba completo)"))
        filtrar_estado(ordenestado)
    elif opcion == 3: 
        costolimite = float (input("Ingrese el precio limite "))
        filtrar_costo(costolimite)
    elif opcion == 4:
        for i in ordenes_reparacion:
            print(i)
    elif opcion == 5:
        print("Adios ")
        break 
    else: 
        print("Opcion invalida ")
        
