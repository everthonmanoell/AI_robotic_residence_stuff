print("\n--- PARTE 1: SEM DESCRITOR ---")

class Conta:
    saldo = 1  # atributo de CLASSE
    outro = [1,2,3]

c = Conta()
c2 = Conta()
c3 = Conta()

print("Classe Conta __dict__:", Conta.__dict__)
print("Instância c __dict__:", c.__dict__)

print("c.saldo:", c.saldo)       # busca na classe (1)
print(id(c),"c.outro:", c.outro, id(c.outro))       # busca na classe (1)
print(id(c2),"c2.outro:", c2.outro,id(c.outro))       # busca na classe (1)
print(id(c3),"c3.outro:", c3.outro,id(c.outro))       # busca na classe (1)
print("Conta.saldo:", Conta.saldo)

print("\n--- Criando atributo de instância ---")
c.saldo = 200

print("Classe Conta __dict__:", Conta.__dict__)
print("Instância c __dict__:", c.__dict__)

print("c.saldo:", c.saldo)       # busca na instância (200)
print("Conta.saldo:", Conta.saldo)  # classe continua com 1

print("\n--- PARTE 2: DESCRITOR COM INIT ---")

class NonNegative:
    def __init__(self, nome):
        self.nome = nome
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.nome, 0)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.nome} não pode ser negativo")
        instance.__dict__[self.nome] = value

class Conta:
    saldo = NonNegative("saldo")   # descritor NA CLASSE
    def __init__(self, saldo):
        self.saldo = saldo         # chama __set__

c1 = Conta(100)

print("Classe Conta __dict__:", Conta.__dict__)
print("Instância c1 __dict__:", c1.__dict__)

print("c1.saldo:", c1.saldo)   # 100

print("\n--- Tentando atribuir valor inválido ---")
try:
    c1.saldo = -50
except ValueError as e:
    print("Erro:", e)

print("Instância c1 __dict__:", c1.__dict__)


print("\n--- PARTE 3: DESCRITOR SEM INIT ---")

class Conta:
    saldo = NonNegative("saldo")   # descritor NA CLASSE
    def __init__(self):
        pass

c2 = Conta()

print("Classe Conta __dict__:", Conta.__dict__)
print("Instância c2 __dict__:", c2.__dict__)

print("c2.saldo (antes de atribuir):", c2.saldo)  # fallback 0 do __get__

print("\n--- Agora atribuímos ---")
c2.saldo = 250    # chama __set__
print("Instância c2 __dict__:", c2.__dict__)
print("c2.saldo:", c2.saldo)