class Animal:
    nombre = "Michi"
    especie = "Felino"
    edad = 2
    color = "Blanco y negro"
    
    def comer(self):
        print(f"El {self.nombre} esta comiendo")
        
    def presentar(self):
        print(f"El {self.nombre}, tiene {self.edad} años y es color {self.color}")

gato = Animal()
print(gato.nombre)
print(gato.especie)
gato.comer()
gato.presentar()