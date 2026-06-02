class Vehiculo:
    marca = "Honda"
    modelo = "MT06"
    color = "Rojo"
    velocidad = 150

    def arrancar(self):
        print(f"La {self.marca} arranco con una velocidad de {self.velocidad}")

    def frenar(self):
        print(f"La {self.marca} {self.modelo} freno")

    def información(self):
        print(moto.marca, moto.modelo, moto.color, moto.velocidad)

moto = Vehiculo()
print(moto.marca, moto.modelo, moto.color, moto.velocidad)
moto.arrancar()
moto.frenar()