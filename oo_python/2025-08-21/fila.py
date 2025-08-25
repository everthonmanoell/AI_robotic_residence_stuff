class Fila:
    def __init__(self, *elementos):
        self.fila = list(elementos)

    def entrar(self, elemento):
        self.fila.append(elemento)
    def estender(self,lista_elementos):
        self.fila.extend(lista_elementos)
    def sair(self):
        if self.tamanho_atual() > 0:
            return self.fila.pop(0)
    def vazia(self):
        return self.tamanho_atual() == 0
    def tamanho_atual(self):
        return len(self.fila)
    # def __sub__(self, outra_fila):
    #     return self
    def __eq__(self, outra_fila): # eq = equal -> é chamado quando chama o == entre dois objetos
        return self.fila == outra_fila.fila
    def __lt__(self, outra_fila): # lt = left thant -> é chamado quando uma o < entre dois objetos
        return len(self.fila) < len(outra_fila.fila)
    def __add__(self,outra_fila): # add = add -> é chamado quando usa o + entre dois objetos. 
        nova_fila = Fila()
        nova_fila.fila = self.fila + outra_fila.fila
        return nova_fila
    def __str__(self):
        return f'Fila: {self.fila}'
if __name__ == '__main__':
    f = Fila()
    print(f)
    f = Fila(1)
    print(f)
    f = Fila(1,2,3)
    print(f)
    f.entrar(15)
    f1 = Fila(1,2,3)
    print(f1, type(f1))
    f2 = Fila(4,5,6)
    print(f2, type(f2))
    f3 = f1+f2
    print(f3, type(f3))
    f3.estender([7,8,9,10])
    print(f3, type(f3))
    # f4 = f3 - f2
    # print(hash(f4), hash(f3))
    # print(f3 is f4)
    # print(f3 == f4)

    f1 = Fila(1,2,3,4,5)
    f2 = Fila(1,2,3)
    print(f1, type(f1))
    print(f2, type(f2))
    print(f1 < f2)
    # print(f1, hash(f1), type(f1))
    # print(f2, hash(f2), type(f2))
    # print(f1 is f2, f1==f2)

