# criando uma classe
class Pessoa:
    
    def __init__(self):
        self.nome = "Jake"
    
    def __str__(self) -> str:
        return "A pessoa criada se chama " + self.nome
    
pessoa_1 = Pessoa()
pessoa_1.nome = "Angelo"
print(pessoa_1)

pessoa_2 = Pessoa()
print(pessoa_2)


class Cao:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self) -> str:
        return "O cão criada se chama " + self.nome
    
    
cao = Cao("Jake")
print(cao)