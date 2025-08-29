#NÃO É UM SINGLETON

class X:
    pass

if __name__ == '__main__':
    x1 = X()
    x2 = X()
    x3 = X()
    print(x1,x2,x3)
    print(id(x1),id(x2),id(x3))
    print(x1 is x2)
    x1 = X()
    print(x1,x2,x3)
    print(id(x1),id(x2),id(x3))