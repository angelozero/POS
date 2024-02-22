class Carro:
    
    def __init__(self):
        self.buzina = "bibi"
    
    def __str__(self) -> str:
        return "A buzina do carro faz " + self.buzinar()
    
    def buzinar(self):
        return self.buzina