class Array:
    def __init__(self, tamanho):
        self.__tamanho = int(tamanho)
        if self.__tamanho > 0:
            self.__elementos = [None] * self.__tamanho
            self.__qtde_elementos = 0
        else:
            raise ValueError('O tamanho do Array precisa ser um número.')
    
    def __getitem__(self, posicao):
        return self.obter(posicao)
    
    def __setitem__(self, posicao, valor):
        return self.incluir(posicao, valor)
    
    def __len__(self):
        # return self.__qtde_elementos
        return self.__tamanho

    def total_elementos(self):
        return self.__qtde_elementos
    
    #incluir(1, 12) coloca 12 na posição 0 da lista (1ª posição)
    def incluir(self, posicao, valor):
        if posicao > 0 and posicao <= self.__tamanho:
            if self.__elementos[posicao-1] == None:    
                self.__qtde_elementos += 1
            if valor == None:
                self.__qtde_elementos -= 1
            self.__elementos[posicao-1] = valor
        else:
            raise IndexError('Tentando incluir elemento fora do intervalo do array.')
    
    def obter(self, posicao):
        if posicao > 0 and posicao <= self.__tamanho:
            return self.__elementos[posicao-1]
        else:
            raise IndexError('Tentando acessar elemento fora do intervalo do array.')    

    def __eq__(self, outro_array):
        if type(self) != type(outro_array):
            return False
        if len(self) != len(outro_array):
            return False
        if self.__qtde_elementos != outro_array.total_elementos():
            return False
        for i in range(len(self)):
            if self.__elementos[i] != outro_array[i+1]:
                return False
        return True

    def __iter__(self):
        for i in range(self.__tamanho):
            yield self.__elementos[i]
    def __contains__(self, elemento):
        return elemento in self.__elementos
    def __str__(self):
        return f'< {', '.join([str(x) for x in self.__elementos])} > ({self.__qtde_elementos})'
        # return str(self.__elementos)


if __name__ == '__main__':
    a = Array(4)
    b = Array(4)
    a[1] = 2
    b[1] = 2
    print(a, type(a), id(a))
    print(b, type(b), id(b))
    print(a == b)
    # print(2 in a)
    # for elemento in a:
    #     print(elemento)
    L = [1,2,3]
    M = [1,2,3]
    # print(L, type(L), id(L))
    # print(M, type(M), id(M))
    # print(L == M)
    # print(2 in L)
    # for elemento in L:
    #     print(elemento)
    # print(a, len(a))
    # # a.incluir(22, 50)
    # a.incluir(2, 50)
    # print(a, len(a))
    # a[1] = 60
    # print(a, len(a))
    # a[2] = 60
    # print(a, len(a))
    # a[2] = None
    # print(a, len(a))
    # a[4] = None
    # print(a, len(a))
    
    # print(a.obter(1), a[1])
    # print(a.obter(2), a[2])
    # print(len([1,2,3]))
    # print(len(a))
