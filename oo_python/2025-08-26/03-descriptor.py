class Positivo:
    def __set_name__(self, owner, name):
        print('entrei aqui no __set_name__')
        self.private_name = "_" + name
    def __get__(self, instance, owner):
        print('entrei aqui no __get__')
        if instance is None:
            return self
        return getattr(instance,self.private_name, None)
    def __set__(self, instance, value):
        print('entrei aqui no __set__')
        if value < 0:
            raise ValueError("Valor deve ser positivo!")
        setattr(instance, self.private_name, value)

class Conta: 
    saldo = Positivo()
    def __init__(self, saldo):
        print('aqui no __init__ de Conta')
        self.saldo = saldo

if __name__ == '__main__':

    c = Conta(200)
    print('antes de imprimir c.saldo')
    print(c.saldo)
    print('depois de imprimir c.saldo')
    print('antes de atribuir novo valor para c.saldo')
    c.saldo = 20
    print('depois de atribuir novo valor para c.saldo')
    print(c.saldo)
    # print(c.saldo, type(c.saldo), type(c._saldo), type(Conta.saldo))
    # c.saldo = -120
    # print(c.saldo)