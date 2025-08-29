from observer import Observer, Sujeito


class EstacaoMeteorologica(Sujeito): 
    def __init__(self):
        super().__init__()
        self.temperatura = None
    def set_temperatura(self, valor):
        self.temperatura = valor
        self.notificar(temperatura = self.temperatura)

class DisplayCondicoesClimaticas(Observer):
    def atualizar(self, *args, **kwargs):
        temperatura_atual = kwargs.get('temperatura', 0)
        print(f'Temperatura atual: {temperatura_atual}ºC')

if __name__ == '__main__':
    estacao = EstacaoMeteorologica()
    display = DisplayCondicoesClimaticas()
    estacao.adicionar_observer(display)
    estacao.set_temperatura(28.6)
    print(estacao.temperatura)