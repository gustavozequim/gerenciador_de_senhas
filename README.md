# GERENCIADOR DE SENHAS
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-concluído-green)
Gerenciador de senhas que utiliza hash para criptografia.

## Como funciona:
  - Funciona via CLI;
  - Possui as seguintes funções:
      - 1 - Salvar nova senha:
          - Cria uma chave (ela será utilizada para acessar está senha) e salva ela do db/chave.key;
          - Solicita o domínio, aqui você digitará o domínio do site ou app que utiliza essa senha;
          - Solicita a senha.
      - 2 - Consulta de senhas:
          - Solicita o domínio da senha;
          - Solicita a chave gerada, que está guardada em db/chave.key.
      - 3 - Para a execução.

## Estrutura
```
gerenciador_de_senhas/
    L src/
      L settings/
        L settings.py
      L password_views.py
      L passwords.py
      L template.py
    L .gitignore
    L LICENSE
    L README.md
    L pyproject.toml
    L requiremnts.txt

```

## Utilização:
  - Para utilizar, clone o projeto no seu PC:
  ```
    - git clone https://github.com/gustavozequim/gerenciador_de_senhas
  ```
  - Em seguida, instale o requirements.txt:
      - Obs: Antes de instalar o requirements.txt, crie uma venv no Python:
        ```
          - python -m venv <escolha um nome para o ambiente>
          - python .\<nome do ambiente>\Sripts\Activate        
        ```
        Isso garante que você irá instalar as dependências apenas naquele projeto, não afetam nenhum de seus outros projetos.
  
  Após a configuração do ambiente virtual, e inicialização do mesmo, instale as dependências:
  ```
    - pip install -r requirements.txt
  ```
  - Renomeie o arquivo ".env_model" para ".env", e altere os caminhos
  
  - Execute:
  ```
    - python -m src.template
  ```
  - Insira as informações desejadas, e pronto. Acesse o db/ e verá uma estrutura assim:
  ```
    db/
      L chave.key
      L Senhas.txt
  ```
  - Senhas.txt terá o domínio junto da hash equivalente à senha. Ex:
  ```
    youtube.com | gAAAAABpw_0CC4UD32stjqMYj9f9KYJ-4mA2bsW2j9vO2aT_OxHP22CxI9OGywV4OyRAUZj9U8OFDxvAaK12Y0fpQATM80obVN9cg==q | 25/03/2026-12:19:30
  ```
  - chave.key terá a sua chave de acesso à senha, que fará a descriptografia e te fornecerá a mesma. Ex:
  ```
    E8qmx5NEJ6SiUl5ccdyyzjlnhCDasdaNZ6hiBsIoAHtivtcHtp4=
  ```
Pronto, agora suas senhas estão seguras e anotadas.
