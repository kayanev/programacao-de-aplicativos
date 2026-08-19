"""Crie uma classe mãe Carro com os atributos marca, modelo e combustivel (iniciado em 100), 
além do método acelerar().  
Crie a classe filha CarroEletrico que herda de Carro.  
No __init__ da classe CarroEletrico, utilize super().__init__() e adicione a variável bateria iniciada 
em 100 (em vez do combustível tradicional).  
Sobrescreva o método acelerar() na classe CarroEletrico: Cada vez que o carro acelerar, 
deve consumir 5% da bateria (verifique se há bateria suficiente disponível antes de acelerar).
Exiba a mensagem: "O carro elétrico acelerou silenciosamente! Bateria restante: X%".
Crie um método recarregar() que restaura o nível da bateria para 100.Crie o método painel() 
adaptado para exibir a porcentagem de bateria do veículo elétrico.
"""

class Carro:
    def __init__(self, marca, modelo, combustivel : int = 0):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = combustivel

    def acelerar(self):
        if self.combustivel > 0:
            self.combustivel -= 5
            print(f"O {self.modelo} acelerou!")
            print(f"Combustível atual: {self.combustivel}")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = 100

    def acelerar(self):
        if self.bateria > 0:
            self.bateria -= 5
            print("O carro elétrico acelerou silenciosamente!")
            print(f"Bateria atual: {self.bateria}%")

    def recarregar(self):
        if self.bateria < 100:
            self.bateria = 100
            print(f"O carro foi recarregado, bateria atual: {self.bateria}")

        else:
            print("A bateria já está cheia!")

    def painel(self):
        print(f"Quantidade de bateria: {self.bateria}")

carro_eletrico = CarroEletrico("Marca", "Modelo", 100)

carro_eletrico.painel()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.acelerar()
carro_eletrico.recarregar()
