class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def info(self):
        print(f'Marca: {self.marca} Modelo: {self.modelo} Cor: {self.cor}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, quantidade_rodas, quantidade_portas, motor, combustivel):
        super().__init__(marca, modelo, cor)
        self.quantidade_rodas = quantidade_rodas
        self.quantidade_portas = quantidade_portas
        self.motor = motor
        self.combustivel = combustivel

    def info(self):
        super().info()
        print(f'Rodas: {self.quantidade_rodas} Portas: {self.quantidade_portas} Motor: {self.motor} Combustível: {self.combustivel}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, cilindrada):
        super().__init__(marca, modelo, cor)
        self.cilindrada = cilindrada
    def info(self):
        super().info()
        print(f'Cilindrada: {self.cilindrada}')
        print(f'{super().info()} Cilindrada: {self.cilindrada}')




