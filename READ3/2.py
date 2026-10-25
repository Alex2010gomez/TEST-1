class recursodigital():
    def __init__(self,codigo,titulo,categoria,autor,anio,disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible
    
    def resumen(self):
        print(f"Codigo : {self.codigo} | Titulo : {self.titulo} | Categoria {self.categoria} | Disponible {self.disponible}")

recursos = [
    recursodigital(codigo=201, titulo="Introducción a Python", categoria="E-book", autor="Gabriel López", anio=2023, disponible=True),
    recursodigital(codigo=202, titulo="Machine Learning Avanzado", categoria="AudioLibro", autor="Elena Gómez", anio=2024, disponible=False),
    recursodigital(codigo=203, titulo="Diseño de Interfaces UX/UI", categoria="PDF", autor="Carlos Martínez", anio=2022, disponible=True),
    recursodigital(codigo=204, titulo="Bases de Datos SQL y NoSQL", categoria="E-book", autor="Sofía Rodríguez", anio=2025, disponible=True),
    recursodigital(codigo=205, titulo="Guía de Ciberseguridad Familiar", categoria="PDF", autor="Diego Fernández", anio=2021, disponible=False),
    recursodigital(codigo=206, titulo="Desarrollo Web con React", categoria="E-book", autor="Mariana Costa", anio=2024, disponible=True),
    recursodigital(codigo=207, titulo="Historia de la Computación", categoria="AudioLibro", autor="Javier López", anio=2019, disponible=True),
    recursodigital(codigo=208, titulo="Metodologías Ágiles: Scrum", categoria="PDF", autor="Ana Benítez", anio=2023, disponible=False)
]

def buscar(objetos):
    palabra = str(input("Ingrese el El titulo o parte de el : "))
    resultados = []
    for i in objetos:
        if palabra.lower() in i.titulo.lower():
            resultados.append(i)
    
    if not resultados:
        print ("Sin coincidencias ")
    else:
        print("Resultados : ")
        for o in resultados:
            o.resumen()

buscar(recursos)