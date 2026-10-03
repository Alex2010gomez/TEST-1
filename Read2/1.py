inventario_equipos = [ #Lista con diccionarios 
    {"inventario": "INV-001","tipo": "Notebook","marca": "Dell","estado": "Disponible","año": 2023},
    {"inventario": "INV-002","tipo": "Monitor","marca": "LG","estado": "Disponible","año": 2022},
    {"inventario": "INV-003","tipo": "Impresora","marca": "HP","estado": "En reparación","año": 2021},
    {"inventario": "INV-004","tipo": "Proyector","marca": "Epson","estado": "Disponible","año": 2020},
    {"inventario": "INV-005","tipo": "Notebook","marca": "Lenovo","estado": "Baja","año": 2018},
    {"inventario": "INV-006","tipo": "Servidor","marca": "Dell","estado": "Disponible","año": 2024},
    {"inventario": "INV-007","tipo": "Tablet","marca": "Apple","estado": "En reparación","año": 2023},
    {"inventario": "INV-008","tipo": "Switch de Red","marca": "Cisco","estado": "Baja","año": 2017 }
]

seleccion = int(input("Ingrese el año minimo "))
filtro1 = []

for i in inventario_equipos: #Recorre la lista 
    if 'Disponible' in i["estado"] and seleccion <= i["año"]: # Si esta en estado "Disponible " y es menor que el año seleccionado
        filtro1.append(i) #Se agrega a la lista con resultados 
    
if not filtro1 : #Si esta vacia 
    print(" Sin coincidencias ")
else : # Si no 
    for o in filtro1:
        print(o)