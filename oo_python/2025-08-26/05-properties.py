class Carro:
    def __init__(self, modelo, ano_fabricacao, km_rodados):
        self.__modelo = modelo
        self.__ano_fabricacao = ano_fabricacao
        self.__km_rodados = km_rodados
        self.__pneus = 'pirelli r14'
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def kms(self):
        return self.__km_rodados
    
    @property
    def pneus(self):
        return self.__pneus
    
    @pneus.setter
    def pneus(self, novo_conjunto_pneus):
        self.__pneus = novo_conjunto_pneus
    
    def dirigir(self, distancia_em_kms):
        if distancia_em_kms > 0: 
            self.__km_rodados += distancia_em_kms
        else:
            raise ValueError('Distância inválida')

if __name__ == '__main__':
    c = Carro('celta', 2018, 68000)
    print(c.modelo, c.kms, c.pneus)
    c.dirigir(2000)
    print(c.modelo, c.kms, c.pneus)
    c.pneus = 'goodyear r15'
    print(c.modelo, c.kms, c.pneus)
    