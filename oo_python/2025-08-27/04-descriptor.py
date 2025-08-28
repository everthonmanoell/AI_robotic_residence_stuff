class NaoNegativo:
    def __set_name__(self, owner, name):
        print('entrei aqui no __set_name__')
        self.private_name = "_" + name
    def __get__(self, instance, owner):
        print('entrei aqui no __get__')
        if instance is None:
            return self
        return getattr(instance,self.private_name, None)
    #c.saldo = 10
    def __set__(self, instance, value):
        print('entrei aqui no __set__')
        if value < 0:
            raise ValueError("Valor deve ser positivo!")
        setattr(instance, self.private_name, value)

class Conta:
    saldo = NaoNegativo()
    
if __name__ == '__main__' :
    # o = NaoNegativo()
    # print(o.__dict__)
    # o.saldo = -10
    # print(o.__dict__)
    c = Conta()
    # print(Conta.saldo.private_name)
    print(c.__dict__)

    # # print(Conta.__dict__)
    c.saldo = 10
    print(c.__dict__)