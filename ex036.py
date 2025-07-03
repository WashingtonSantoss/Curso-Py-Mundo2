#Escreva um programa para aprovar um empréstimo bancário para comprar uma casa. Perguntando ao cliente, 
#valor da casa, o salario, e em quantos anos ele quer pagar, a prestação mensal não pode exceder 30%
#do salario, se não o empréstimo será negado !

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Quantos anos deseja pagar? "))
parcela_mensal = valor_casa / (anos * 12)

porcentagem_minima = salario*0.3 # Ou salario * 30 / 100

if parcela_mensal > porcentagem_minima:
    print(f"Foi NEGADO pois a parcela é de {parcela_mensal} e 30% do seu salario é {porcentagem_minima}")
else:
    print(f"Foi APROVADO, com uma parcela de {parcela_mensal}")