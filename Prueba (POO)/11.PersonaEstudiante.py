class Persona:
    nombre = "Ana"
    edad = 18
    ciudad = "Bucaramanga"
    ocupación = "Estudiante"
    
    def estudiar(self):
        print(f"{self.nombre} es una estudiante")
        
    def presentarse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}")

estudiante = Persona()
print(estudiante.nombre, estudiante.edad, estudiante.ciudad, estudiante.ocupación)
estudiante.estudiar()
estudiante.presentarse()