"""Adicione um novo parâmetro chamado idade (inteiro) no método construtor (__init__),
que deve iniciar sempre em 0 caso não seja passado na criação;
Crie um método chamado aniversario() que aumenta a idade do animal em 1 ano 
e imprime uma mensagem comemorativa (ex: "O [nome] fez [idade] anos!");
Instancie 3 animais de espécies diferentes. 
Faça-os emitir som e envelhecer pelo menos duas vezes cada.
"""

class Animal:
    def __init__(self, nome : str, barulho : str, idade : int):
        self.nome = nome
        self.barulho = barulho
        self.idade = idade

    def faz_barulho(self):
        print(f"{self.nome} faz {self.barulho}")

    def aniversario(self):
        self.idade += 1
        print(f"O {self.nome} fez {self.idade} anos!")

def main():
    gato = Animal("Gato","Miau!",2)
    cachorro = Animal("Cachorro","Au Au!",4)
    lobo = Animal("Lobo","Auu!",5)

    cachorro.aniversario()
    cachorro.aniversario()
    cachorro.aniversario()
    cachorro.faz_barulho()
    gato.aniversario()
    gato.aniversario()
    gato.aniversario()
    gato.faz_barulho()
    lobo.aniversario()
    lobo.aniversario()
    lobo.faz_barulho()

if __name__ == "__main__":
    main()

