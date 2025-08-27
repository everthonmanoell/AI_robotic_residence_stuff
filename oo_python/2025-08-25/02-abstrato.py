from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def method(self):
        return 'em Super.method'
    def delegate(self):
        return self.action()
    @abstractmethod
    def action(self):
        pass

class Inheritor(Super):
    pass
class Replacer(Super):
    def method(self):
        return 'em Replacer.method'
class Extender(Super):
    def method(self):
        s = 'iniciando Extender.method | '
        s += super().method()
        s += ' | encerrando Extender.method'
        return s
class Provider(Super):
    def action(self):
        return 'em Provider.action'

if __name__ == '__main__':
    # s = Super()
    # i = Inheritor()
    # r = Replacer()
    # e = Extender()
    p = Provider()
    print(p.delegate())
