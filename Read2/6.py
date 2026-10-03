class DispositivoRed:  #Clase principal 
    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock): #Atributos
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad = velocidad_mbps
        self.precio = precio
        self.stock = stock

    def mostrardatos(self): #Metodo para mostar los datos 
        print(f"Código: {self.codigo} | Tipo: {self.tipo} | Marca: {self.marca} | Velocidad: {self.velocidad} Mbps | Precio: ${self.precio} | Stock: {self.stock}")

    def haystock(self): # Metodo para validar si hay stock 
        return self.stock > 0


def filter_velocidad(lista_dispositivos): # Funcion para filtrar por velocidad 
    filtrado = []
    v_minima = int(input("Ingrese la velocidad mínima: ")) #Velocidad Minima
    v_maxima = int(input("Ingrese la velocidad máxima: ")) #Velocidad maxima 
    
    for i in lista_dispositivos: # Recorre la lista 
        if v_minima <= i.velocidad <= v_maxima: # Si la velocidad esta entre la velocidad minima y la maxima continua 
            if i.haystock(): #Si lo que  continuo tiene stock se agrega a la lista con los resultados que coincidieron 
                filtrado.append(i)
                
    if not filtrado: #Si no hay nada 
        print("Sin resultados.") 
    else: #Si no 
        for o in filtrado:
            o.mostrardatos() 

def buscar_codigo(lista_dispositivos): # Funcion para buscar por codigo 
    filtro = [] 
    cod = input("Ingrese el código del dispositivo: ").strip().upper() #.strip() elimina caracteres especiales y .upper() pone todas las letras en mayusculas 
    
    for i in lista_dispositivos: # Recorre la lista 
        if cod in i.codigo.upper(): # si lo ingresado anteriormente coincide con algo de la lista lo agrega a la lista con los posibles resultados , contempla que solo se ingrese una parte del codigo 
            filtro.append(i)
            
    if not filtro: #Si no hay nada 
        print("Dispositivo no encontrado.")
    else: #Si no 
        for o in filtro:
            o.mostrardatos()
        return filtro

def presupuesto(lista_dispositivos): #Funcion para filtrar por limite de presupuesto 
    filtro = []
    maxprecio = float(input("Ingrese el presupuesto máximo: "))
    
    for i in lista_dispositivos: #Recorre la lista de objetos 
        if i.precio <= maxprecio: #Si lo que se ingreso anteriormete es mayor o igual al valor del objeto se agrega a la lista con resultados 
            filtro.append(i)
            
    if not filtro: #Si esta vacia 
        print("Sin coincidencias.")
    else:# Si no 
        for o in filtro:
            o.mostrardatos()
# Lista de objetos , Estos se pasan con el patron clave - valor 
dispositivos = [
    DispositivoRed(codigo="RTR-001", tipo="Router", marca="TP-Link", velocidad_mbps=1200, precio=45000.00, stock=15),
    DispositivoRed(codigo="SWI-042", tipo="Switch", marca="Cisco", velocidad_mbps=1000, precio=120000.00, stock=8),
    DispositivoRed(codigo="USB-WF9", tipo="Adaptador Wi-Fi USB", marca="Mercusys", velocidad_mbps=300, precio=12500.00, stock=50),
    DispositivoRed(codigo="REP-883", tipo="Repetidor", marca="Xiaomi", velocidad_mbps=750, precio=28000.00, stock=22),
    DispositivoRed(codigo="PCI-ETH1", tipo="Placa de Red PCIe", marca="Asus", velocidad_mbps=10000, precio=85000.00, stock=5),
    DispositivoRed(codigo="MSH-300", tipo="Sistema Mesh", marca="Tenda", velocidad_mbps=1167, precio=160000.00, stock=10)
]

filter_velocidad(dispositivos)
buscar_codigo(dispositivos)
presupuesto(dispositivos)
