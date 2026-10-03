lista_libros = [
    {"ISBN": "978-950-731-923-5","título": "Ficciones","autor": "Jorge Luis Borges","disponible": True},
    {"ISBN": "978-842-067-177-2","título": "El túnel","autor": "Ernesto Sabato","disponible": False},
    {"ISBN": "978-950-511-313-2","título": "Rayuela","autor": "Julio Cortázar","disponible": True},
    {"ISBN": "978-843-760-494-7","título": "Bodas de sangre","autor": "Federico García Lorca","disponible": True},
    {"ISBN": "978-849-759-220-8","título": "Cien años de soledad","autor": "Gabriel García Márquez","disponible": False}
]

busqueda = str(input("Ingrese el ISBN del libro : "))
resultado = []
for i in lista_libros:
    if busqueda == i["ISBN"] : 
        resultado.append(i)
#else: 
   #print("Libro no encontrado ") Esta estructura muestra mensajes incorrectos debido a que se ejecuta cada vez que el for completa una pasada 
# a mi parecer lo correcto seria evaluar si hay algo en la lista que almacena los resultados , si no lo hay devolver no encontrado

if not resultado:
    print("Libro no encontrado")
else:
    for o in resultado:
        print(f"Libro : {o}")