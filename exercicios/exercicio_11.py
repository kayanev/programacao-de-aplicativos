"""Crie uma classe CofreDigital.
O __init__ deve receber o titular e uma senha (string de 4 dígitos). O atributo senha deve ser privado 
(self.__senha).
O atributo saldo inicia em 0.0 e também deve ser privado (self.__saldo).
Crie o método depositar(valor).
Crie o método sacar(valor, senha_informada) com as funcionalidades 
[ Verificar se a senha_informada é igual à __senha, se a senha estiver correta e houver saldo, 
deduz o valor, se a senha estiver incorreta, exibe: "Senha incorreta! Acesso negado. ]
Tente alterar o saldo e a senha diretamente, sem usar os métodos para entender o encapsulamento faz.
"""
class CofreDigital:
    def __init__(self, titular, senha : str):
        self.__titular = titular
        self.__senha = senha
        self.__saldo = 0.0

    def depositar(self, valor):
        self.valor = valor

        if valor > 0:
            self.__saldo += self.valor
            print(f"Depósito de R${valor:.2f} realizado.")
        
    
    def sacar(self, valor, senha_informada : str):
        if senha_informada != self.__senha:
            print("Senha incorreta! Acesso negado.")

        elif valor > self.__saldo:
            print(f"Saldo insuficiente! Saldo atual: R${self.__saldo:.2f}")

        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")            
        
conta1 = CofreDigital("Selene", "1712")

conta1.depositar(40.0)
conta1.sacar(10.0, "1712")