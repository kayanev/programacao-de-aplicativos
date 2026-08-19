"""Crie uma classe mãe chamada Funcionario com os atributos nome, cpf e salario.
Classe Funcionario:
exibir_dados(): exibe no terminal o nome, CPF e o salário formatado do funcionário. aumentar_salario
(percentual): aumenta o salário do funcionário com base no percentual informado.
Classe filha de Funcionario - Gerente:
Reaproveitar nome, cpf e salario, e adicione o atributo exclusivo setor.
método exclusivo receber_bonificacao(), que concede um aumento adicional fixo de 10% sobre 
o salário atual do gerente e exibe uma mensagem comemorativa.
"""

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir_dados(self):
        print(f"Funcionário: {self.nome}\nCPF: {self.cpf}\nSalário: {self.salario}")

    def aumentar_salario(self, percentual):
        self.percentual = percentual

        aumento = self.salario * self.percentual
        salario_novo = self.salario + aumento
        self.salario = salario_novo

        print(f"{self.nome} recebeu um aumento! Seu salário agora é de: {self.salario}")
        

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self, aumento_fixo = 0.10):
        self.aumentar_salario(0.10)

        print(f"Parabéns {self.nome} do setor {self.setor}! Você recebeu uma bonificação, seu salário agora é de: {self.salario}")

funcionario = Funcionario("Melinda", "122-725-765-52", 2000)
gerente = Gerente("Selene", "102-243-654-25", 3500, "2")

funcionario.aumentar_salario(0.05)
funcionario.exibir_dados()
gerente.aumentar_salario(0.10)
gerente.receber_bonificacao()
gerente.exibir_dados()