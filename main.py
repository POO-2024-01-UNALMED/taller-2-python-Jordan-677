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
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        asientos=[]
        asientos.append(Asiento)
        self.marca=marca
        self.motor=motor
        self.registro=registro
        cantidadCreados=cantidadCreados
        

    def cantidadAsientos(self,asientos):
        return len(asientos)
    
    def verificarIntegridad():
        if(Auto.registro==Asiento.registro and Asiento.registro==Motor.registro):
            return "Las piezas son originales"
        else: return "Las piezas no son originales"
        