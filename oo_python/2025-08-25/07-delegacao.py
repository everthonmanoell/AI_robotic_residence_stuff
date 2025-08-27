from abc import ABCMeta, abstractmethod


class Backend(metaclass = ABCMeta):
    @abstractmethod
    def carregar(self, caminho):
        pass
    @abstractmethod
    def salvar(self, caminho):
        pass
class BackendPNG(Backend):
    def carregar(self, caminho):
        print(f'[PNG] Abrindo imagem em {caminho}')
    def salvar(self, caminho):
        print(f'[PNG] Salvando em {caminho}')

class BackendJPG(Backend):
    def carregar(self, caminho):
        print(f'[JPG] Abrindo imagem em {caminho}')
    def salvar(self, caminho):
        print(f'[JPG] Salvando em {caminho}')

class ProcessadorImagens:
    def __init__(self, backend):
        self.backend = backend # composição
    def abrir_imagem(self, caminho):
        self.backend.carregar(caminho) #delegação
    def salvar_imagem(self, caminho):
        self.backend.salvar(caminho) #delegação

if __name__ == '__main__':
    b = Backend()
    png = BackendPNG()
    jpg = BackendJPG()
    proc_png = ProcessadorImagens(png)
    proc_jpg = ProcessadorImagens(jpg)
    proc_png.abrir_imagem('C:\\caminho...')
    proc_jpg.abrir_imagem('C:\\caminho...')    