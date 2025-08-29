#SINGLETON
class X:
    _instancia = None
    def __new__(cls, *args, **kwargs):
        print(f'__new__ X {args} {kwargs} {cls}')
        # if not cls._instancia:
        if cls._instancia == None:#cls._instancia == X._instancia
            print('Se entrou aqui, é a primeira vez que tentou criar o objeto')
            cls._instancia = super().__new__(cls)
        else:
            print('Se entrou aqui, está tentando criar objeto, mas já foi inicializado')
        return cls._instancia
    def __init__(self, valor):
        print(f'__init__ com valor {valor} - {self}')
        self.valor = valor
        # if not hasattr(self, 'inicializado'):
        #     print('só entra aqui 1 vez, quando o objeto nunca foi inicializado')
        #     self.valor = valor
        #     self.inicializado = True
        # else:
        #     print(f'no else de __init__')

class A:
    v = 151515

if __name__ == '__main__':
    # print(A.v)
    # a = A()
    # print(a.v)
    x1 = X(1)
    print(x1.valor)
    # print('---')
    x2 = X(2)
    print(x1.valor)
    x3 = X(3)
    print(x1.valor)
    # #getattr
    # #setattr
    # #hasattr
    print('--------')
    print(hasattr(x1, 'valor'), hasattr(x2, 'valor'), hasattr(x3, 'valor'))# posso fazer x1.informacao?
    print(x1.valor, x2.valor, x3.valor)
    print(id(x1),id(x2),id(x3))
    print((x1 is x2) and (x2 is x3) and (x1 is x3))
    
    # print(hasattr(x1, 'inicializado'), hasattr(x2, 'inicializado'), hasattr(x3, 'inicializado'))# posso fazer x1.informacao?
    # print(x1.inicializado, x2.inicializado, x3.inicializado)
    # # print(x1,x2,x3)
    # # print(id(x1),id(x2),id(x3))
    # # print(x1 is x2)
    # # x1 = X()
    # # print(x1,x2,x3)
    # # print(id(x1),id(x2),id(x3))