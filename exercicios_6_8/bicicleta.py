class Bicicleta:
    def __init__(self, modelo : str, velocidade : int = 0):
        self.modelo = modelo
        self.velocidade = velocidade
    
    def pedalar(self):
        if self.velocidade < 60:
            self.velocidade += 5

            print(f"A bike {self.modelo} acelerou! Velocidade: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print(f"Reduzindo... Velocidade: {self.velocidade} km/h")
        else:
            print("A bicicleta já está totalmente parada!")

    def radar_velocidade(self):
        print(f"A velocidade atual é: {self.velocidade}km.")
    
def main():
    bicicleta = Bicicleta("Caloi")
    bicicleta.pedalar()
    bicicleta.pedalar()
    bicicleta.radar_velocidade()
    bicicleta.frear()
    bicicleta.frear()
    bicicleta.frear()

if __name__ == "__main__":
    main()