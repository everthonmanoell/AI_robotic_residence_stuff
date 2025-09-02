#Um Observer observa um Sujeito (estamos falando de objetos)
#um observer quer ter ciência quando algo muda no sujeito

class Sujeito:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer: 'Observer'):
        self._observers.append(observer)
    
    def remover_observer(self, observer):
        self._observers.remove(observer)
    
    def notificar(self, dados):
        for obs in self._observers:
            obs.atualizar(dados)

class Observer:
    def atualizar(self, dados):
        raise NotImplementedError
    
class PrintObserver(Observer):
    def __init__(self, nome):
        self.nome = nome
    def atualizar(self, dados):
        print(f'{self.nome} recebeu notificação com dados {dados}')

sujeito = Sujeito()
o1, o2 = PrintObserver('Teste 1'), PrintObserver('Observador 2')
sujeito.adicionar_observer(o1)
sujeito.adicionar_observer(o2)
sujeito.notificar([1,2,3,4])
sujeito.remover_observer(o1)
print('---')
sujeito.notificar([1,3,4])