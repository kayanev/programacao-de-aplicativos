"""Crie uma classe mãe chamada Animal com os atributos nome e especie no método __init__, 
e um método fazer_som() que imprime uma mensagem genérica;
Crie três classes filhas que herdam de Animal: Cachorro, Gato e Vaca;
Utilize a função super().__init__() no método construtor de cada classe filha para definir a espécie 
automaticamente (ex: "Canino", "Felino", "Bovino") e adicione o atributo raca;
Sobrescreva o método fazer_som() em cada uma das classes filhas para exibir o som característico 
de cada animal (ex: "Au Au!", "Miau!", "Muuu!");
Instancie um objeto de cada classe e chame o método fazer_som() para demonstrar o funcionamento do 
Polimorfismo
"""

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print(f"O {self.nome} da especie {self.especie} faz som")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} faz Au Au!")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome ,"Felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} faz Miau!")

class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome , "Bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} da raça {self.raca} faz Muuu!")

cachorro = Cachorro("Teca", "Vira lata")
gato = Gato("Elza", "Siames")
vaca = Vaca("Mimosa", "Holandesa")

cachorro.fazer_som()
gato.fazer_som()
vaca.fazer_som()

