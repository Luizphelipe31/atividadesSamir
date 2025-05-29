import random
import string

tamanho = int(input("Digite o tamanho da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choices(caracteres, k=tamanho))
print("Senha gerada:", senha)


import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Usuário Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API. Código: ", resposta.status_code)
gerar_usuario()




import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP inválido.")
        else:
            print("=== Endereço Encontrado ===")
            print("Rua    :", dados.get("logradouro", "Não disponível"))
            print("Bairro :", dados.get("bairro", "Não disponível"))
            print("Cidade :", dados.get("localidade", "Não disponível"))
            print("Estado :", dados.get("uf", "Não disponível"))
    else:
        print("Erro ao acessar a API.")

cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)




import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            print("=== Cotação Atual ===")
            print("Moeda        :", cotacao['name'])
            print("Valor Atual  : R$", cotacao['bid'])
            print("Valor Mínimo : R$", cotacao['low'])
            print("Valor Máximo : R$", cotacao['high'])
            print("Data/Hora    :", cotacao['create_date'])
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao acessar a API.")

codigo_moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo_moeda)
