class Semaforo:
    def __init__(self):
        self.estado_atual = 'VERMELHO'

    def troca(self):
        if self.estado_atual == 'VERMELHO':
            self.estado_atual = 'VERDE'
        elif self.estado_atual == 'VERDE':
            self.estado_atual = 'AMARELO'
        elif self.estado_atual == 'AMARELO':
            self.estado_atual = 'VERMELHO'
    def __str__(self):
        return f'Estado atual: {self.estado_atual}'

if __name__ == '__main__':
    s = Semaforo()
    for i in range(10):
        print(f't={i} {s}')
        s.troca()