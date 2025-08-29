from transitions import Machine

estados = ['PARADO', 'SUBINDO', 'DESCENDO']
transicoes = [
    # parado -> parado
    {
        'trigger': 'parar',
        'source': ['SUBINDO', 'DESCENDO', 'PARADO'],
        'dest': 'PARADO'
    },

    # subir
    {
        'trigger': 'subir',
        'source': 'PARADO',
        'dest':    'SUBINDO'
    },
    #descer
    {
        'trigger':  'descer',
        'source': 'PARADO',
        'dest':'DESCENDO'
    }
]
class Elevador:
    def on_enter_PARADO(self):
        print('O elevador parou')
    def on_enter_SUBINDO(self):
        print('O elevador está subindo')
    def on_enter_DESCENDO(self):
        print('O elevador está descendo')

    def on_exit_PARADO(self):
        print('O elevador vai sair do estado PARADO')
    def on_exit_SUBINDO(self):
        print('O elevador vai sair do estado SUBINDO')
    def on_exit_DESCENDO(self):
        print('O elevador vai sair do estado DESCENDO')



elevador = Elevador()

maquina = Machine (
    model = elevador,
    states = estados,
    transitions= transicoes,
    initial= 'PARADO'
)


if __name__ == '__main__':
    print(elevador.state)
    elevador.subir()
    print(elevador.state)
    elevador.parar()
    print(elevador.state)
    elevador.descer()
    print(elevador.state)
    elevador.parar()
    print(elevador.state)
    elevador.parar()
    print(elevador.state)