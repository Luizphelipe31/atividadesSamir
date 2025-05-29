def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

conta = 100.0
porcentagem = 10.0
valor_gorjeta = calcular_gorjeta(conta, porcentagem)
print(f"Gorjeta de {porcentagem}% sobre R${conta:.2f} é R${valor_gorjeta:.2f}")






def eh_palindromo(texto):
    texto_limpo = ''.join(letra.lower() for letra in texto if letra.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
    print(eh_palindromo("A base do teto desaba"))
print(eh_palindromo("Python"))
print(eh_palindromo("ana"))
print(eh_palindromo("ovo"))
print(eh_palindromo("radar"))
print(eh_palindromo("casa"))
print(eh_palindromo("nada"))







while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha == "sair":
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte!")
    break








from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias
print(idade_em_dias(2000))





