## Consumindo API HG-Brasil
Esse é um software que consome a API de finanças da HG-Brasil, a ideia desse projeto é colocar os conceitos de programação e finanças que estou aprendendo ao longo de minha jornada.
# :heavy_dollar_sign: Sobre o Projeto
Esse projeto consiste em criar um ambiente de visualização no terminal dos demais indices, moedas, titulos financeiros e ações do mercado de capitais brasileiro. Projeto ainda em andamento.
# :small_airplane: Como rodar o projeto
Para rodar esse projeto você precisara do <a href="https://git-scm.com/downloads">GIT</a> para clonar o repositório, <a href="https://www.python.org/">Python</a> e uma chave no <a href="https://hgbrasil.com/status/finance">HG-Brasil Finance</a> que será usada como parâmetro para puxar as informações.
```
# Clonar o repositório:
$ git clone https://github.com/marqosPrado/consult_API_HG.git

# Acesse a pasta no terminal/cmd
$ cd consult_API_HG
```
# :key: Configurando o projeto
Com sua chave em mãos, entre no diretório 'config' e entre no arquivo 'config.py', na função chave substitua o valor da variável 'HG_API_KEY' pela sua chave:
# 
<img height=400 weight=400 src="https://github.com/marqosPrado/assets/blob/main/consult_api/foto1.png?raw=true">
    
Nesse mesmo arquivo você pode configurar o tempo de atualização dos dados na variável ATUALIZACAO (valores em segundos):
# 
<img height=400 weight=400 src="https://github.com/marqosPrado/assets/blob/main/consult_api/foto2.png">

# Como executar o projeto

Linux e MacOS - Entre na pasta 'APP/', e execute o código:
```
$ python3 index.py
```
Windows:
```
$ python index.py
```

Quando executar deve aparecer o terminal assim:
#    
<img src="https://github.com/marqosPrado/assets/blob/main/consult_api/foto3.png">

lembrando que este projeto está em fase inicial, planejo colocar mais informação e até criar um site para exibir as informação de um jeito mais organizado.
