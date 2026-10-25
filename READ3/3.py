class componente():
    def __init__(self, codigo, nombre, tipo, marca, stock,ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock 
        self.ubicacion = ubicacion 
        
    def haystock(self):
        if self.stock > 0 :
            return True
        elif 0 >= self.stock :
            return False
        else: 
            return False 
        
    def mostrardatos(self):
        print(f"Codigo : {self.codigo} | Nombre : {self.nombre} ")
        print(f"Tipo : {self.tipo} | Marca : {self.marca} | Stock disponible {self.stock} | Ubicacion {self.ubicacion}")

componentes = [
componente(codigo="RAM001",nombre= "Memoria RAM 16GB",tipo="Memoria", marca="Corsair",stock= 25, ubicacion="Estante A1"),
componente(codigo="SSD002", nombre="Disco Sólido 1TB NVMe",tipo= "Almacenamiento",  marca="Samsung",stock= 14, ubicacion="Estante A2"),
componente(codigo="GPU003", nombre="Tarjeta Gráfica RTX 4060", tipo="Video",  marca="ASUS",stock= 5, ubicacion="Estante B1"),
componente(codigo="CPU004", nombre="Procesador Core i7", tipo="Procesador",  marca="Intel",stock= 0, ubicacion="Estante B2"),
componente(codigo="MOBO05", nombre="Placa Madre B650M", tipo="Placa Base",  marca="MSI", stock=8, ubicacion="Estante C1"),
componente(codigo="PSU006", nombre="Fuente 750W Certificada", tipo="Energía",  marca="EVGA", stock=12, ubicacion="Estante C2"),
componente(codigo="COOL07", nombre="Disipador CPU Air", tipo="Refrigeración",  marca="Noctua", stock=18, ubicacion="Estante D1"),
componente(codigo="CASE08", nombre="Gabinete Mid-Tower", tipo="Chasis",  marca="NZXT",stock= 0, ubicacion="Estante D2"),
componente(codigo="MON009", nombre="Monitor 24'' 144Hz", tipo="Monitor",  marca="LG", stock=7, ubicacion="Depósito General"),
componente(codigo="PER010", nombre="Teclado Mecánico RGB", tipo="Periférico",  marca="Logitech", stock=30,ubicacion= "Mostrador")
]

def buscartipo(componentes):
    posibles_resultados = []
    cantidad_resultados = 0
    mayor_resultado = None
    tipocomponente = str(input("Escriba el tipo de componente : ")).lower().strip()
    cantidad_stock = int(input("Ingrese la cantidad de stock minima : "))
    for i in componentes:
        if i.tipo.lower() == tipocomponente and i.stock >= cantidad_stock:
            posibles_resultados.append(i)
            cantidad_resultados += 1
            if mayor_resultado is None or i.stock > mayor_resultado.stock:
                mayor_resultado = i
                
    if not posibles_resultados:
        print("Sin resultados ")
    else:
        print(f"Componentes que cumplen con las condiciones : {cantidad_resultados}")
        for o in posibles_resultados:
            o.mostrardatos()
            
        print("Componente con mayor stock : ")
        mayor_resultado.mostrardatos()
                
buscartipo(componentes)
    

        