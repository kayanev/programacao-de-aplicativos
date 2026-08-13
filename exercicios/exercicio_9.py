"""Crie uma classe Livro com os atributos: titulo:str, autor:str e paginas:int;
Implemente o método especial def __str__(self): para retornar uma string formatada:
"Livro: '[titulo]' por [autor] [paginas] pgs"
Crie o método comparar_tamanho(outro_livro) que recebe outro objeto Livro e imprime 
qual dos dois livros tem mais páginas;
Instancie 2 livros, use o print() direto nas variáveis para testar o __str__    
e compare o tamanho entre eles.
"""

class Livro:
    def __init__(self, titulo : str, autor : str, paginas : int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor} de {self.paginas} pgs"
    
    def comparar_tamanho(self, outro_livro):
        if self.paginas < outro_livro.paginas:
            diferenca = outro_livro.paginas - self.paginas
            print(f"O livro {outro_livro.titulo} tem {diferenca} páginas a mais que o outro, totalizando {outro_livro.paginas} pgs.")
        
        elif self.paginas > outro_livro.paginas:
            diferenca = self.paginas - outro_livro.paginas
            print(f"O {outro_livro.titulo} tem {diferenca} páginas a menos que o outro, totalizando {outro_livro.paginas} pgs.")

        
        

def main():
    livro1 = Livro("Querida Konbini", "Sayaka Murata", 152)
    livro2 = Livro("Declínio de um homem", "Osamu Dazai", 160)

    #print(livro1)
    livro2.comparar_tamanho(livro1)
    livro1.comparar_tamanho(livro2)

if __name__ == "__main__":
    main()
