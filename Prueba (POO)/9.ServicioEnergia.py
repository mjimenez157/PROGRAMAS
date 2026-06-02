class Servicio:
    tipo = "Energia"
    proveedor = "Empresa electrica"
    servicio = "Electricidad"
    precio = 150000

    def activar(self):
        print(f"El servicio de {self.tipo} esta activado")

    def información(self):
        print(f"El servicio es de {self.servicio}, su proveedor es {self.proveedor} y su costo es de {self.precio}")

energia = Servicio()
energia.activar()
energia.información()