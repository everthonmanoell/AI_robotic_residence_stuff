class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def info(self):
        print(f'Tipo: {self.tipo} Potência: {self.potencia}CV')
class Carro:
    def __init__(self, marca, modelo, cor, quantidade_rodas, quantidade_portas, motor: Motor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.quantidade_rodas = quantidade_rodas
        self.quantidade_portas = quantidade_portas
        self.motor = motor
        self.combustivel = combustivel

    def info(self):
        print(f'Marca: {self.marca} Modelo: {self.modelo} Cor: {self.cor}')
        print(f'Rodas: {self.quantidade_rodas} Portas: {self.quantidade_portas} Combustível: {self.combustivel}')
        self.motor.info()


if __name__ == '__main__':
    motor1 = Motor('V8', 600)
    carro1 = Carro('Ford', 'Mustang', 'Vermelho', 4, 2, motor1, 'Gasolina')
    carro1.info()