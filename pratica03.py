idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto.")
elif idade >= 60:
    print("Você é um idoso.")









peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
print("Classificação:", classificacao)





temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (c, f ou k): ")
destino = input("Digite a unidade de destino (c, f ou k): ")
resultado = 0

if origem == "c" and destino == "f":
    resultado = (temperatura * 9/5) + 32
elif origem == "c" and destino == "k":
    resultado = temperatura + 273.15
elif origem == "f" and destino == "c":
    resultado = (temperatura - 32) * 5/9
elif origem == "f" and destino == "k":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "k" and destino == "c":
    resultado = temperatura - 273.15
elif origem == "k" and destino == "f":
    resultado = (temperatura - 273.15) * 9/5 + 32
elif origem == destino:
    resultado = temperatura
else:
    print("Tente novamente, temperatura inválida!")
if origem != destino and resultado != 0:
    print("Temperatura convertida:", round(resultado, 2), destino)
elif origem == destino:
    print("Temperatura continua igual:", round(resultado, 2), destino)





ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, "não é bissexto.")









