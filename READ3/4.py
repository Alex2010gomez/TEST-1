class videojuegos():
    def __init__(self,codigo,titulo,genero,plataforma,anio,horas_estimadas):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas
    
    def mostrar_datos(self):
        print(f"Codigo : {self.codigo} | Titulo : {self.titulo} | Genero : {self.genero}")
        print(f"Plataforma : {self.plataforma} | Año : {self.anio} | Cantidad de horas estimadas : {self.horas_estimadas}")
    
    def es_del_genero(self,genero):
        if self.genero == genero:
            return True
        else:
            return False
    
    def supera_horas(self,horas):
        if self.horas_estimadas >= horas:
            return True
        else:
            return False

lista_videojuegos = [
    videojuegos(codigo="VJ001", titulo="The Legend of Zelda: Breath of the Wild", genero="Aventura", plataforma="Nintendo Switch", anio=2017, horas_estimadas=50),
    videojuegos(codigo="VJ002", titulo="Elden Ring", genero="Acción RPG", plataforma="PC / PlayStation / Xbox", anio=2022, horas_estimadas=60),
    videojuegos(codigo="VJ003", titulo="Red Dead Redemption 2", genero="Acción-Aventura", plataforma="PC / PlayStation / Xbox", anio=2018, horas_estimadas=60),
    videojuegos(codigo="VJ004", titulo="The Witcher 3: Wild Hunt", genero="RPG", plataforma="PC / PlayStation / Xbox", anio=2015, horas_estimadas=50),
    videojuegos(codigo="VJ005", titulo="Minecraft", genero="Sandbox", plataforma="Multiplataforma", anio=2011, horas_estimadas=100),
    videojuegos(codigo="VJ006", titulo="Hades", genero="Roguelike", plataforma="PC / Switch / PlayStation / Xbox", anio=2020, horas_estimadas=25),
    videojuegos(codigo="VJ007", titulo="Cyberpunk 2077", genero="Acción RPG", plataforma="PC / PlayStation / Xbox", anio=2020, horas_estimadas=30),
    videojuegos(codigo="VJ008", titulo="God of War Ragnarök", genero="Acción-Aventura", plataforma="PlayStation 4 / PlayStation 5", anio=2022, horas_estimadas=35)
]
def buscar_por_genero():
    buscargen = str (input("Ingrese el genero a buscar "))
    resultadosgen = []
    for i in lista_videojuegos:
        if i.genero.lower() == buscargen.lower():
            resultadosgen.append(i)
    if not resultadosgen:
        print("Sin resultados")
    else:
        for o in resultadosgen:
            o.mostrar_datos()

def buscar_horas():
    horas = float(input("Ingrese la cantidad de horas minimas : "))
    superados = []
    for i in lista_videojuegos:
        if i.supera_horas(horas) == True:
            superados.append(i)
    if not superados:
        print("Sin resultados ")
    else:
        for o in superados:
            o.mostrar_datos()
    
def buscar_por_codigo(cod):
    
    for i in lista_videojuegos:
        if i.codigo.lower() == cod : 
            return i
        
    return None

buscar_por_genero()
buscar_horas()

cod = str (input("Ingrese el codigo ")).lower()

if buscar_por_codigo(cod) == None:
    print("Sin resultados de la busqueda por codigo ")
else:
    resultadocodigo = buscar_por_codigo(cod)
    resultadocodigo.mostrar_datos()