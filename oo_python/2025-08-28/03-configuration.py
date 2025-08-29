from dataclasses import dataclass

from singleton import Singleton


@dataclass
class ConfiguracaoSistema(Singleton):
    nome_usuario : str


if __name__ == '__main__':
    config1 = ConfiguracaoSistema('teste')
    config2 = ConfiguracaoSistema('outro')
    print(config1,config2)
    print(id(config1),id(config2))
    print(type(config1),type(config2))