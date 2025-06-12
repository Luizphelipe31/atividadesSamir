import statistics

tempos = []

with open('log.txt', 'r') as arquivo:
    for linha in arquivo:
        tempo = float(linha.strip())
        tempos.append(tempo)

media = statistics.mean(tempos)
desvio_padrao = statistics.stdev(tempos)

print("Média dos tempos: {:.2f}".format(media))
print("Desvio padrão dos tempos: {:.2f}".format(desvio_padrao))





import csv

pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Alice", 30, "São Paulo"],
    ["Bruno", 25, "Rio de Janeiro"],
    ["Carla", 27, "Belo Horizonte"]
]

with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(pessoas)
print("Arquivo CSV criado com sucesso!")


import csv

with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)








import json

pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

with open('pessoa.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print("Arquivo JSON criado!")

with open('pessoa.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
print("Nome:", dados["nome"])
print("Idade:", dados["idade"])
print("Cidade:", dados["cidade"])



