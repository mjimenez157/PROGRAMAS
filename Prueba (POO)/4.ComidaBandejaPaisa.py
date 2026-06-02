class Comida:
    nombre = "Bandeja paisa"
    origen = "Colombia"
    ciudad = "Bucaramanga"
    precio = 25000
    
    def preparar(self):
        print(f"La {self.nombre} se esta preparando")
        
    def servir(self):
        print(f"La {self.nombre}, esta servida y su costo es de {self.precio}")

comida = BandejaPaisa()
print(comida.nombre)
comida.preparar()
comida.servir()