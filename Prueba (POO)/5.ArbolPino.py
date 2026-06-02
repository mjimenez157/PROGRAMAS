class Arbol:
    tipo = "Pino"
    altura = "30 metros"
    edad = 10
    color = "Verde"
    
    def plantar(self):
        print(f"El {self.tipo} fue plantado hace {self.edad} años")
    
    def altura(self):
        print(f"El {self.tipo}, tiene una altura de {self.altura} y es color es {self.color}")

pino = Arbol()
print(pino.tipo)
pino.plantar()
pino.altura()