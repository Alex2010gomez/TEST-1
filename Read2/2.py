repuestos = [# Lista con diccionarios
    {"codigo": "R01", "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 45.0, "stock": 5},
    {"codigo": "R02", "descripcion": "Memoria RAM 8GB DDR4", "categoria": "Memoria", "marca": "Crucial", "precio": 30.0, "stock": 0},
    {"codigo": "R03", "descripcion": "Disco Duro 1TB SATA", "categoria": "Almacenamiento", "marca": "Western Digital", "precio": 60.0, "stock": 3},
    {"codigo": "R04", "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 80.0, "stock": 2},
    {"codigo": "R05", "descripcion": "Fuente de poder 500W", "categoria": "Energía", "marca": "Gigabyte", "precio": 55.0, "stock": 4},
    {"codigo": "R06", "descripcion": "Placa de video GTX 1650", "categoria": "Video", "marca": "Nvidia", "precio": 150.0, "stock": 0},
    {"codigo": "R07", "descripcion": "Cooler CPU Fan", "categoria": "Refrigeración", "marca": "Cooler Master", "precio": 25.0, "stock": 10},
    {"codigo": "R08", "descripcion": "Gabinete Gamer RGB", "categoria": "Gabinetes", "marca": "Redragon", "precio": 70.0, "stock": 1},
]

entrada = str(input("Ingrese la descripcion o parte de ella ")).lower().strip() #.lower() reduce a minusculas y .strip() elimina espacios al inicio y fin junto a caracteres especiales 
filtro1 = []

for i in repuestos: # Recorre la lista con diccionarios 
    if entrada in i["descripcion"].lower(): #Si lo ingresado anteriormente esta en la descripcion en minuscula se agrega a la lista con resultados 
        filtro1.append(i)
        
    stock = [o for o in repuestos if o["stock"] > 0] #Metodo de filtrado por compresion(creo que se llamaba haci) Si stock es mayor a 0 
    cantidad_stock = len(stock) #No recuerdo que quise hacer pero funciona ;V

if len(filtro1) == 0 :
    print(" Sin coincidencias ")
else:
    print("Cantidad coincidencias : ",len(filtro1))
    print("Cantidad de elementos con stock : ", cantidad_stock)
    for s in filtro1 : 
        print(s)