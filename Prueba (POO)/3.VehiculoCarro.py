class Vehiculo:
    tipo = "Camioneta"
    marca = "Toyota"
    modelo = "Fortuner"
    color = "Blanco"

    def arrancar(self):
        print(f"La {self.tipo} {self.modelo} arranco")

    def frenar(self):
        print(f"La {self.marca} {self.modelo} freno")

    def información(self):
        print(carro.tipo, carro.marca, carro.modelo, carro.color)

carro = Vehiculo()
print(carro.marca, carro.modelo, carro.color)
carro.arrancar()
carro.frenar()