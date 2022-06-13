class Persona ():

    def __init__(self, nombre = "",edad ="",dni= ""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


    def mostrar(self):
        print (f"el nombre es : {self.nombre}")
        print (f"La edad es: : {self.edad}")
        print (f"El dni es : {self.dni}")

    def esMayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
class Cuenta():
    
    def __init__(self, titular,cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        
        print(f"El titular es: {self.titular}")
        print(f"El saldo es: {self.cantidad}")

    def ingresar(self,cantidad):
        self.cantidad = cantidad + self.cantidad

    def retirar(self,cantidad):
        self.cantidad = self.cantidad - cantidad


persona1 = Persona




cuenta_uno = Cuenta("Ezequias Bonvissuto")

cuenta_uno.mostrar()
cuenta_uno.ingresar(500)
cuenta_uno.mostrar()

cuenta_uno.retirar(300)
cuenta_uno.mostrar()


