asistencia = [] #Lista vacia 

nuevo1 = str(input("Ingrese el nombre del primer alumno: ")) #Primer input 
nuevo2 = str(input("Ingrese el nombre del segundo alumno:  ")) #Segundo input
asistencia.append(nuevo1) #Se agrega el primer input a la lista
asistencia.append(nuevo2) #Se agrega el segundo input a la lista
for i in asistencia: #Se recorre la lista
    print("Alumno",i) #Se imprime la lista