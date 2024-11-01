from .settings.settings import DIRETORIO_BD

import base64
import hashlib
from pathlib import Path
import string, secrets

from cryptography.fernet import Fernet, InvalidToken


class FernetHasher:
    STRING_ALEATORIA = string.ascii_letters + str(string.punctuation)
    caminho_chave = Path(__file__).parent
    caminho_chave = Path(DIRETORIO_BD)
    caminho_chave.mkdir(exist_ok=True)

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()
        
        self.fernet = Fernet(key)

    @classmethod
    def _cria_string_aleatoria(cls, quantidade_caracteres: int=10):
        caracter = ''
        for char in range(quantidade_caracteres):
            caracter = caracter + secrets.choice(cls.STRING_ALEATORIA)
        
        return caracter

    @classmethod
    def cria_chave(cls, arquivo: bool=False):
        valor = cls._cria_string_aleatoria()
        hasher = hashlib.sha256(valor.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        if arquivo:
            return key, cls.guarda_chaves(key)
        return key, None

    @classmethod
    def guarda_chaves(cls, key):
        file = 'chave.key'
        while Path(cls.caminho_chave / file).exists():
            file = f'chave_{cls._cria_string_aleatoria(5)}.key'

        with open(cls.caminho_chave / file, 'wb') as arquivo:
            arquivo.write(key)

        return cls.caminho_chave / file

    def encripta(self, valor):
        if not isinstance(valor, bytes):
            valor = valor.encode()
        return self.fernet.encrypt(valor)
    
    def decripta(self, valor):
        if not isinstance(valor, bytes):
            valor = valor.encode()
        try:
            return self.fernet.decrypt(valor).decode()
        except InvalidToken:
            return 'Token utilizado é inválido'
