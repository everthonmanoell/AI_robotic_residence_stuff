class A:
    def a(self):
        print('m de A')
class B:
    def b(self):
        print('m de B')
class C:
    def c(self):
        print('m de C')
class D:
    def m(self):
        print('m de D')
class E(B,C,D,A):
    pass
    # def m(self):
    #     print('m de E')

if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    print(a, type(a), isinstance(a,A), isinstance(a, A))
    print(b, type(b), isinstance(b,B), isinstance(b, A))
    print(c, type(c), isinstance(c,C), isinstance(c, A))
    print(d, type(d), isinstance(d,D), isinstance(d, A))
    print(e, type(e), isinstance(e,E), isinstance(e, A), isinstance(e, B), isinstance(e, C), isinstance(e, D))

    # a.m()
    # b.m()
    # c.m()
    # d.m()
    e.m()
    print(E.mro())
    print(str.mro())
    print(list.mro())
    print(int.mro())
    