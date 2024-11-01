from datetime import datetime as dt
from pathlib import Path

from src.settings.settings import DIRETORIO_BD


class ModeloBase:
    caminho_bd = Path(DIRETORIO_BD)
    caminho_bd.mkdir(exist_ok=True)

    def save(self):
        caminho_tabela = Path(
            self.caminho_bd / f'{self.__class__.__name__}.txt'
        )
        if not caminho_tabela.exists():
            caminho_tabela.touch()
        senha = ' | '.join(list(map(str, self.__dict__.values())))
        with open(caminho_tabela, 'a') as arquivo:
            arquivo.write(senha)
            arquivo.write('\n')

    @classmethod
    def get(cls):
        caminho_tabela = Path(
            cls.caminho_bd / f'{cls.__name__}.txt'
        )
        if not caminho_tabela.exists():
            caminho_tabela.touch()
        with open(caminho_tabela, 'r') as arquivo:
            texto = arquivo.readlines()
        results = []
        atributos = vars(cls())

        for linha in texto:
            valores_separados = linha.split('|')
            tmp_dict = dict(zip(atributos, valores_separados))
            results.append(tmp_dict)

        return results



class Senhas(ModeloBase):

    def __init__(self, domiminio=None, senha=None):
        self.dominio = domiminio
        self.senha = senha
        self.creat_at = dt.now().strftime('%d/%m/%Y-%H:%M:%S')
