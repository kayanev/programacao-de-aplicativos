"""Crie uma classe OrdemDeServico com os atributos: cliente e descricao;
Crie um atributo de classe chamado total_os_criadas = 0 e um atributo chamado os_abertas = 0;
Sempre que uma nova OrdemDeServico for instanciada (__init__), o atributo de classe 
total_os_criadas e os_abertas devem ser incrementadas em 1, e o objeto ordem de serviço atual 
deve receber o valor de total_os_criadas como seu id_os;
Crie o atributo status que inicia como "Aberta";
Crie o método finalizar_os() que altera o status para "Concluída" e diminua em 1 o valor de os_abertas;
Instancie 3 ordens de serviço e conclua uma;
Crie um método capaz de verificar quantas ordens estão abertas.
"""
class OrdemDeServico:
    id_os = 0
    total_os_criadas = 0
    os_aberta_count = 0

    def __init__(self, cliente, descricao):
        OrdemDeServico.id_os = self.id_os

        self.cliente = cliente
        self.descricao = descricao

        OrdemDeServico.total_os_criadas += 1
        OrdemDeServico.os_aberta_count += 1

        self.id_os = self.total_os_criadas
        self.status = "Aberta"

    def finalizar_os(self):
        if self.status == "Aberta":
            self.status = "Concluída"
            OrdemDeServico.os_aberta_count -= 1
            
            print(f"Ordem de serviço finalizada. OS sobrando: {self.os_aberta_count}")

    def os_abertas(self):
        print(f"Ordens de Serviço abertas no momento: {self.os_aberta_count}")
    
cliente1 = OrdemDeServico("Selene", "Compras")
cliente2 = OrdemDeServico("Melinda", "Vendas")
cliente3 = OrdemDeServico("Castyel", "Trocas")

cliente1.os_abertas()
cliente1.finalizar_os()




        
        