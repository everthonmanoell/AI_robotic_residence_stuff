from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, nome):
        self.nome = nome
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return 'Au au!'
class Gato(Animal):
    def falar(self):
        return 'Miau!'
class Galinha(Animal):
    def falar(self):
        return 'Cocoricó!'

if __name__ == '__main__':
    # A = [Cachorro('Rex'), Gato('Mingau'), Galinha('Pintadinha'), Animal('teste')]
    A = [Cachorro('Rex'), Gato('Mingau'), Galinha('Pintadinha')]
    for animal in A: 
        print(animal.nome, "fala: ", animal.falar())