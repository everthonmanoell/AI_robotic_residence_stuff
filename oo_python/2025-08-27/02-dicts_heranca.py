class A:
    a = '12'
class B(A):
    b = [1,2,3]
class C(B):
    c = {'teste':'teste'}
class D(C):
    d = 12
    x = 15
    y = 10
    def __init__(self, v):
        self.y = v
class E(D):
    e = 20
    def __init__(self, v):
        super().__init__(v+15)
        self.x = v

if __name__ == '__main__' :
    classes = [A,B,C,D,E]
    a = A()
    b = B()
    c = C()
    d = D(99)
    e = E(80)
    objetos = [a,b,c,d,e]
    for i in range(len(objetos)):
        print(objetos[i], classes[i])
        print('Dict do objeto:', objetos[i].__dict__)
        print('Dict da classe:',classes[i].__dict__)
        print('---------------------')

    print(e.x, e.e, e.d, e.y, e.c, e.b, e.a)
    print(e.__dict__)
    e.a = 598
    e.novo_atributo = 'qualquer coisa'
    print(e.__dict__)
    print(e.x, e.e, e.d, e.y, e.c, e.b, e.a)
