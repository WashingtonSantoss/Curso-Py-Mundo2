#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, 
#se é a hora de se alistar ou se já passou do tempo, e mostrar tambem o tempo que falta para se alistar ou que passou do prazo

nascimento = int(input("Digite o ano do seu nascimento: "))
base = int(input("Qual ano está fazendo a consulta agora ? "))

idade = base - nascimento 


while idade < 0:
    idade = int(input("Digite uma idade valida."))
    nascimento = int(input("Digite o ano do seu nascimento: "))
    base = int(input("Qual ano está fazendo a consulta agora ? "))
    idade = base - nascimento 

print(f"Você tem {idade} anos,", end="")

if idade == 17 or idade == 18:
    print(" Está na hora de fazer o alistamento!")
elif idade < 17 and idade > 0:
    tempo = 17 - idade
    print(f" Falta {tempo} anos para você conseguir se alistar.")
else:
    tempo = idade - 18
    print(f" Se você não se alistou, Você está {tempo} anos atrasado para se alistar.")

