#AAQWERABSFAPSJINDAJKBSF
from abc import ABC 
class persona(ABC): #Clase abstracta 
    def __init__(self,nombre,apellido,dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    
    @property  #Metodo para ver el nombre
    def GetNombre(self):
        return self.__nombre
    @property # Metodo para ver el apellido 
    def GetApellido(self):
        return self.__apellido
    @property #Metodo para ver el dni 
    def GetDNI (self):
        return self.__dni
#Clase hija 
class alumno(persona):
    def __init__(self, nombre, apellido, dni,curso,promedio):
        super().__init__(nombre,apellido,dni)
        self.__curso = curso
        self.__promedio = promedio
    
    @property #Metodo para ver el curso
    def getcurso(self):
        return self.__curso

    @property #Metodo para ver el promedio 
    def getpromedio(self):
        return self.__promedio
    #Metodo para poder ver todos los datos en conjunto 
    def verdatos(self):
        print(f"Nombre : {self.GetNombre} | Apellido: {self.GetApellido} | DNI : {self.GetDNI} | Curso : {self.getcurso} | Promedio : {self.getpromedio}")

test = alumno("Alex","Gómez",50050053,43,8)
test.verdatos()