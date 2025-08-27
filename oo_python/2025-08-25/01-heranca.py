class Super:
    def method(self):
        return 'em Super.method'
    def delegate(self):
        return self.action()
    def action(self):
        raise NotImplementedError('action precisa ser definida em alguma subclasse')
    # def delegate(outro_nome_para_o_self_aqui):
    #     return outro_nome_para_o_self_aqui.action()
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
    s = Super()
    i = Inheritor()
    r = Replacer()
    e = Extender()
    p = Provider()
    T = (s,i,r,e,p)
    for objeto in T:
        print(type(objeto), objeto.method(), 'delegate' in dir(objeto), 'action' in dir(objeto))
        print('---')
    # for nome in dir(p):
    #     print(nome)
    print(p.delegate())