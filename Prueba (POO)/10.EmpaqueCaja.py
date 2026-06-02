class Empaque:
    material = "Cartón"
    peso = "1kg"
    color = "Marrón"
    tamaño = "Grande"
    
    def abrir(self):
        print("la caja esta abierta")
        
    def mostrar(self):
        print(f"Es de {self.material}, pesa {self.peso}, es color {self.color}, y es {self.tamaño}")

caja = Empaque()
caja.abrir()
caja.mostrar()