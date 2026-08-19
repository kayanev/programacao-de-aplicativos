"""Para finalizar os conceitos de POO, vamos criar um sistema de gerenciamento de acervo de biblioteca 
do zero, vamos começar declarando a estrutura de dados (Classes e Objetos) que vamos utilizar:

Classe Mãe - ItemBiblioteca
Atributos: titulo (str), codigo (int) e disponivel (bool, iniciada como True).
Métodos: emprestar() # disponivel -> False, devolver() # disponivel -> True

Classe Filha de ItemBiblioteca - Livro
Atributos: herda os atributos da mãe, adiciona autor (str) e num_paginas (int)

Classe - Usuario
Atributos: nome (str) e itens_emprestados (lista vazia []).
Métodos: 
pegar_item(item) # verifica se o item da biblioteca está disponível. Se sim, chama o método emprestar() 
do item e adiciona o objeto item na lista itens_emprestados, 
devolver_item(item) # verifica se o item está na lista itens_emprestados, chama o método devolver() 
do item e remove-o da lista, 
ver_historico() # exibe o nome do usuário e o título de todos os itens atualmente em sua posse.
"""
class ItemBiblioteca:
    def __init__(self, titulo : str, codigo : int, disponivel : bool = True):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print(f"Desculpe, o livro {self.titulo} não está disponível no momento.")
            return False
        
        self.disponivel = False
        print(f"O livro {self.titulo} está disponível! Livro emprestado.")
        return True

    def devolver(self):
        self.disponivel = True
        print(f"O livro {self.titulo} foi devolvido. Obrigado!")

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor : str, codigo, num_pag : str, disponivel):
        super().__init__(titulo, codigo, disponivel = True)
        self.autor = autor
        self.num_pag = num_pag

        if disponivel == True:
            print(f"O livro {titulo} de {autor} do código {codigo} com {num_pag} páginas está disponível.")
        else:
            print(f"O livro {titulo} de {autor} do código {codigo} com {num_pag} páginas não está disponível.")

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}')"

    def __str__(self):
        return f"{self.titulo}"

    


class Usuario:
    def __init__(self, nome : str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)

        else:
            print("Desculpe, o livro não está disponível no momento.")

    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)

        else:
            print(f"O item {item} não está com esse usuário.")

    def ver_historico(self):
        print(f"Usuário: {self.nome}\nItens emprestados: {self.itens_emprestados}")

livro1 = Livro("Título", "Autor", "1234", "147", True)
usuario = Usuario("Selene")

usuario.pegar_item(livro1)
usuario.ver_historico()
usuario.devolver_item(livro1)
usuario.ver_historico()