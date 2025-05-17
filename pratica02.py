valor_em_reais = 100
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

print("Valor em reais: R$", round(valor_em_reais, 2))
print("Convertido para dólares: US$", round(valor_em_dolar, 2))
print("Convertido para euros: ", round(valor_em_euro, 2))




nome_produto = "Camiseta"
preco_original = 50
porcentagem_desconto = 20

valor_desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - valor_desconto

print("Produto: " + nome_produto)
print("Preço original: R$ " + str(preco_original))
print("Desconto de: " + str(porcentagem_desconto) + "%")
print("Valor do desconto: R$ " + str(valor_desconto))
print("Preço final com desconto: R$ " + str(preco_final))



nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

soma = nota1 + nota2 + nota3
media = soma / 3

print("Nota 1: " + str(nota1))
print("Nota 2: " + str(nota2))
print("Nota 3: " + str(nota3))
print("Média final: " + str(round(media, 2)))




distancia = 300
combustivel = 25
consumo_medio = distancia / combustivel

print("Distância percorrida: " + str(distancia) + " km")
print("Combustível gasto: " + str(combustivel) + " litros")
print("Consumo médio: " + str(round(consumo_medio, 2)) + " km/l")


