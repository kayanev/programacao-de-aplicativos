"""Agora deve ser possível ficar com saldo negativo 
até um limite de R$ 500,00. 
Transações além deste limite devem ser bloqueadas.
Crie o método transferir(valor, conta_destino). 
Este método deve validar se há saldo/limite, 
deduzir o valor da conta atual (self) e chamar 
o método adicionar_saldo da conta_destino, 
antes E depois de efetuar este método, 
mostre o saldo das duas contas no terminal.
"""
class ContaBancaria:
    def __init__(self, titular : str, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def transferir(self, conta_destino, valor):
        if self.saldo >= -500:
            self.saldo -= valor
            conta_destino.adicionar_valor(valor)
            return self.saldo
        else:
            print(f"Você não tem saldo suficiente para realizar a transação.")
    
    def adicionar_valor(self, valor):
        self.saldo += valor
        return self.saldo

    def informacoes(self):
        print(f"{self.titular}\nSaldo ATual: {self.saldo}")

def main():
    
    conta1 = ContaBancaria("Selene", 1000)
    conta2 = ContaBancaria("Melinda", 400)

    conta1.informacoes()
    conta2.informacoes()

    conta1.transferir(conta2, 300)


    conta1.informacoes()
    conta2.informacoes()
    
if __name__ == "__main__":
    main()