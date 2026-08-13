"""Crie um método abastecer(quantidade)
que aumente o nível de combustível. 
Adicione validação: o tanque de combustível 
não pode ultrapassar o limite máximo de 100;
Adicione um parâmetro de quilometragem iniciado 
em 0 no __init__. Cada vez que o
método acelerar() for chamado com sucesso 
(tendo combustível), aumente a quilometragem em 15 km;
Crie um método painel() que exiba o painel do carro atualizado.
"""

class Carro:
    def __init__(self, modelo : str, marca : str, quilometragem : int = 0):
        self.modelo = modelo
        self.marca = marca
        self.quilometragem = quilometragem
        self.combustivel = 50

    def abastecer(self):
        self.quantidade = 10

        if self.combustivel <= 100:
            self.combustivel += self.quantidade
            print(f"O carro foi abastecido, combustível atual: {self.combustivel}")
        
        else:
            "O tanque já está cheio."

    def acelerar(self):
        if self.combustivel > 0:
            self.combustivel -= 5
            self.quilometragem += 15
            print(f"O {self.modelo} acelerou! Quilometragem atual: {self.quilometragem}km")
            print(f"Combustível atual: {self.combustivel}")

        else:
            "Sem combustível disponível."
    
    def painel(self):
        print(f"Quantidade de combustível: {self.combustivel}")
        print(f"Quilometragem atual: {self.quilometragem}km")

def main():
    nivus = Carro("Nivus", "Wolkswagen")

    nivus.abastecer()
    nivus.abastecer()
    nivus.painel()
    nivus.acelerar()
    nivus.acelerar()
    nivus.acelerar()

if __name__ == "__main__":
    main()
