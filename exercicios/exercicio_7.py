class PetVirtual:
    def __init__(self, nome : str, fome : int = 5, felicidade : int = 5):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 2
            print(f"{self.nome} foi alimentado! Fome atual: {self.fome}.")

        else:
            print(f"{self.nome} já está de barriga cheia!")

    def brincar(self):
        self.felicidade += 2
        self.fome += 1
        print(f"Você brincou com {self.nome}! Felicidade: {self.felicidade} | Fome: {self.fome}.")

    def status(self):
        print(f"Nome: {self.nome}\nFome: {self.fome}\nFelicidade: {self.felicidade}")
        if self.fome >= 8:
            print(f"Atenção: {self.nome} precisa comer!")

def main():
    pet = PetVirtual("Elza")

    pet.status()
    pet.brincar()
    pet.brincar()
    pet.alimentar()
    pet.alimentar()
    pet.alimentar()
    pet.status()

if __name__ == "__main__":
    main()