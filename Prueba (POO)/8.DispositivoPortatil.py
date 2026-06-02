class Dispositivo:
    marca = "HP"
    modelo = "Pavilion"
    almacenamiento = "400 GB"
    ram = "6 GB"

    def prender(self): 
        print(f"El dispositivo {self.marca} {self.modelo} esta encendido")
    
    def información(self):
        print(self.almacenamiento, self.ram)

portatil = Dispositivo()
portatil.prender()
portatil.información()