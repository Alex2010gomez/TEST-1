basededatos = []  #Lista vacia 
while True: #Bucle infinito
    diccionario = {} #Diccionario 
    nombre =  str(input("Ingrese un nombre : ")) #Input que pide el nombre
    if nombre == "salir": #Si se ingresa "salir" El bucle corta
        print("Adios")
        break
        #Hay una forma mas corta de agregar un dato pero si lo hago no puedo comparar su valor antes de agregarlo 
    else: #Sino se continua 
        diccionario["nombre"] = nombre #Antes de agregar el dato al diccionario se le da un nombre , luego se agrega
        basededatos.append(diccionario) #Se agrega el diccionario a la lista anteriormete declarada
        print("Agregado correctamente")
        
    print("Alumnos en la lista")    
    for i in basededatos: #Se recorre la lista 
        print(i) #Se imprime la lista
        