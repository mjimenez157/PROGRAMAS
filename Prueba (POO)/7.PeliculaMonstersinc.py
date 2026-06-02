class Pelicula:
    nombre = "Monsters Inc"
    Plataforma = "Disney"
    duración = "95 min"
    año = 2001

    def reproducir(self):
        print(f"La pelicula es {self.nombre} de {self.Plataforma}")

    def información(self):
        print(f"Dura {self.duración} y es del año {self.año}")
        
monstersinc = Pelicula()
monstersinc.reproducir()
monstersinc.información()