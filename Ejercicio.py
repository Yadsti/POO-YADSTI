class person:
    def __init__(self,nombre,apellidos,edad):
        self.Apellidos=apellidos
        self.Nombre=nombre
        self.Edad=edad
    def Mostrarperson(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))
print("Objetos Originales:")
p1 = person("Alfredo", "Moreno Muñoz", 35)
p1.Mostrarperson()
p2 = person("Valeria","Moreno", 1)
p2.Mostrarperson()
p1.Edad= 36
p2.Apellidos = "Moreno Córcoles"
print("Objetos modificados:")
p1.Mostrarperson()
p2.Mostrarperson()
