while True:
    entrada1 = input("Digite o primeiro número: ")
    entrada2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        num1 = float(entrada1)
        num2 = float(entrada2)

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Não pode dividir por zero.")
                continue
            else:
                resultado = num1 / num2
        else:
            print("Erro: Operação inválida. Use +, -, * ou /.")
            continue
        print("Resultado:", resultado)
        break
    except:
        print("Erro: Você precisa digitar números válidos.")







       
       
       
       
        notas = []
while True:
    entrada = input("Digite uma nota de 0 a 10 ou 'fim' para sair: ")
    if entrada == "fim":
        break
    try:
        nota = float(entrada)
        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um número entre 0 e 10.")
    except:
        print("Entrada inválida! Digite um número ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("A média da turma é:", media)
else:
    print("Nenhuma nota válida foi digitada.")











while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha == "sair":
        print("Encerrando o programa.")
        break

    if len(senha) < 8:
        print("Senha muito curta, deve ter pelo menos 8 caracteres.")
        continue

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("A senha deve ter pelo menos um número.")
        continue

    print("Senha forte!")
    break







pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("Esse número é par.")
            pares += 1
        else:
            print("Esse número é ímpar.")
            impares += 1

    except ValueError:
        print("Erro: por favor, digite um número inteiro válido.")
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)




