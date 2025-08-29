class Sujeito:
    def __init__(self):
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)
    
    def remover_observer(self, observer):
        self._observers.remove(observer)
    
    #Assumindo que s é uma variável que tem objeto do tipo Sujeito
    #s.notificar()
    #s.notificar(1)... #s.notificar(1,2,3,4,5)
    #s.notificar(nome = 1)... #s.notificar(nome = 1, cpf = 12345678900)
    #s.notificar(1,2,3,4, nome = 1)... 
    def notificar(self, *args, **kwargs):
        for obs in self._observers:
            obs.atualizar(*args, **kwargs)

class Observer:
    def atualizar(self, *args, **kwargs):
        raise NotImplementedError