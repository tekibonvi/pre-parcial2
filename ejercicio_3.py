class Persona ():

    def __init__(self, nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni


    def mostrar(self):
        print (f"el nombre es : {self.nombre}")
        print (f"el nombre es : {self.edad}")
        print (f"el nombre es : {self.dni}")

    def esMayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
class Cuenta():
    
    def __init__(self):
        pass