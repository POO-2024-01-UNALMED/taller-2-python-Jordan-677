class Asiento:
    def __init__(self,color,precio,registro) :
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if (color=="verde" or color=="amarillo" or color=="rojo" or color=="negro" or color=="blanco" ):
            self.color=color

class Motor:
    def __init__(self,numeroCilidros,tipo,registro):
        self.numeroCilidros=numeroCilidros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if(tipo=="electrico" or tipo=="gasolina"):
            self.tipo=tipo

class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
 
        

    def cantidadAsientos(self):
        asientos=0
        for i in self.asientos:
            if (i!=None):
                asientos+=1
        return asientos        
       
    
    def verificarIntegridad(self):
        
        if(self.asientos.registro!=self.registro):
            return "Las piezas no son originales"
        elif(self.motor.registro!=self.registro):
            return "Las piezas no son originales"
        else: return "Auto original"