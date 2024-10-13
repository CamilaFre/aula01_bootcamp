# Programa para cálculo de bônus com entrada do usuário

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus = float(input("Digite a porcentagem do bônus que você recebeu: "))
valor_do_bonus = float(1000 + salario*bonus)


print(f'Olá {nome}! O valor do seu bonus é de {valor_do_bonus} ')