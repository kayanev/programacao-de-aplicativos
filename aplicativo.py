class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        self.nome = nome
        self.consumo_bateria = consumo_bateria

class Celular:
    def __init__(self, marca, modelo, carga = 100):
        self.marca = marca
        self.modelo = modelo
        self.carga_bateria = carga
        self.ligado = False

    def estado(self, app = None):
        if self.ligado == True and self.carga_bateria:
            if app is not None:
                if self.carga_bateria > app.consumo_bateria:
                    print(f"O {self.marca} {self.modelo} está ligado e possui bateria o suficiente para executar o app.")

                else:
                    print(f"Alerta: bateria insuficiente para executar o aplicativo.")
            else:
                print(f"O celular está ligado. (Nenhum aplicativo selecionado.)")
        else:
            print(f"O {self.marca} {self.modelo} está desligado.")

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        self.carga_bateria -= app.consumo_bateria

        if self.ligado == False:
            print(f"O celular não está ligado.")

        elif self.carga_bateria < app.consumo_bateria:
            "O aplicativo não pode ser executado."

        elif self.carga_bateria <= 0:
            print(f"Bateria insuficiente.")

        elif self.carga_bateria >= app.consumo_bateria:
            print(f"O {app.nome} foi utilizado.")

        else:
            print(f"A bateria atual do telefone é {self.carga_bateria}")

def main():
    celular = Celular("Samsung","S23 Ultra")
    youtube = Aplicativo("YouTube", 10)
    crunchyroll = Aplicativo("Crunchyroll", 8)

    celular.ligar()
    celular.estado(youtube)
    celular.executar_app(youtube)


if __name__ == "__main__":
    main()
            

