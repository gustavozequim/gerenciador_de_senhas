from src.passwords import Senhas
from src.password_views import FernetHasher


acao = input('Digite 1 para salvar nova senha ou digite 2 para ver uma senha salva: ')

match acao:
    case '1':
        if len(Senhas.get()) == 0:
            key, path = FernetHasher.cria_chave(arquivo=True)
            print('Chave criada com sucesso!')
            print(f'Chave: {key.decode("utf-8")}')
            if path:
                print(f'Chave salva em: {path}')
        else:
            key = input('Digite a chave gerada: ')
        dominio = input('Digite o Dominio: ')
        senha = input('Digite a Senha: ')
        fernet_user = FernetHasher(key)
        p1 = Senhas(domiminio=dominio, senha=fernet_user.encripta(senha).decode('utf-8'))
        p1.save()
    case '2':
        dominio = input('Digite o Dominio: ')
        key = input('Digite a chave gerada: ')
        fernet_user = FernetHasher(key)
        data = Senhas.get()
        for dados in data:
            if dominio in dados['dominio']:
                senha = fernet_user.decripta(dados['senha'])
            if senha:
                print(f'Sua senha para {dominio} é: {senha}')
            else:
                print(f'Nenhuma senha encontrada para: {dominio}')
