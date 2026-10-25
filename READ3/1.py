class Ticket_soporte: 
    def __init__(self,numero,usuario,sector,problema,prioridad,estado):
        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado
        
    def mostrardatos(self):
        print(f"Numero : {self.numero} | Usuario : {self.usuario} | Sector : {self.sector}")
        print(f"Problema: {self.problema} | Prioridad : {self.prioridad} | Estado : {self.estado}" )

objetos = [
    Ticket_soporte(numero = 101,usuario = "Lucas Pérez",sector = "Ventas", problema  ="No puede ingresar al CRM",prioridad = "Alta",estado = "Abierto"),
    Ticket_soporte(numero= 102,usuario = "Ana Gómez", sector = "Recursos Humanos",problema = "Instalación de suite de diseño", prioridad = "Baja",estado= "En proceso"),
    Ticket_soporte(numero = 103,usuario = "Carlos Martínez",sector = "Finanzas",problema =  "La laptop no enciende luego de actualización",prioridad= "Crítica",estado=  "Abierto"),
    Ticket_soporte(numero =104,usuario = "Sofía Rodríguez", sector ="Marketing", problema = "Desconexión intermitente del Wi-Fi", prioridad = "Media", estado ="Resuelto"),
    Ticket_soporte(numero=105, usuario="Diego Fernández",sector= "Operaciones",problema= "Creación de correo corporativo para nuevo ingreso",prioridad= "Baja",estado="Abierto"),
    Ticket_soporte(numero=106,usuario="Elena Benítez", sector="Legales", problema="Error al exportar reportes mensuales a PDF", prioridad="Media",estado= "En proceso"),
    Ticket_soporte(numero=107,usuario="Javier López",sector="Sistemas",problema= "Alerta de intento de accesos no autorizados",prioridad= "Crítica",estado= "Cerrado"),
    Ticket_soporte(numero=108,usuario="Mariana Costa",sector= "Atención al Cliente",problema= "La impresora no reconoce el tóner nuevo",prioridad= "Alta",estado="Abierto")
]

def buscar_ticket(objetos):
    ticket_buscado = int(input("Ingrese el numero del ticket: "))
    for i in objetos:
        if ticket_buscado == i.numero: 
            return i  
    
    return None 

def filtrado_estado(objetos):
    contador = 0 
    ticket_estado = []
    for i in objetos:
        if "abierto" == i.estado.lower():
            ticket_estado.append(i)
            contador += 1 
    if not ticket_estado:
        print("Ningun Ticket en estado pendiente ")
    else:
        print(f"Tickets en estado 'Pendiente : {contador}")
        for o in ticket_estado:
            o.mostrardatos()

resultado = buscar_ticket(objetos)
if resultado:
    resultado.mostrardatos()
else:
    print("Sin resultados.")

filtrado_estado(objetos)