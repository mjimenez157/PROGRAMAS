class Libro:
    nombre = "100 años de soledad"
    origen = "Colombia"
    autor = "Gabriel Garcia Marquez"
    paginas = 500
    editorial = "alfaguara"
    
    def comprar(self):
        print(f"Usted compro {self.nombre} para leer")
        
    def información(self):
        print(f"Su autor es {self.autor}, esta novela tiene {self.paginas}, su editorial es {self.editorial} y su origen es {self.origen}")

novela = Libro()
print(novela.nombre)
novela.comprar()
novela.información()