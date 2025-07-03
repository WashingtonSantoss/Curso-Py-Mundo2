#Escreva um programa que leia um número inteiro qualquer e peça o usuario escolher qual será a base de conversão
# 1 Binario
# 2 Octal
# 3 Hexadecimal

numero = int(input("Digite um numero inteiro: "))
print(''' 
[1] Para binario
[2] Para Octal
[3] Para Hexadecimal
''')

opcao = int(input("Digite a conversão que deseja fazer: "))

while opcao > 3 or opcao < 1:
    opcao = int(input("Escolha somente uma das 3 opções: "))

print(''' 
[0] Resposta com Prefixo
[1] Resposta sem Prefixo
''')
opcao2 = int(input("Digite 0 ou 1: "))

if opcao2 == 0:
    if opcao == 1:
        print("Seu numero em binario é {}".format(bin(numero)))
    elif opcao == 2:
        print("Seu numero em octal é {}".format(oct(numero))) 
    else:
        print(f"Seu numero em hexadecimal é {hex(numero)}") 
else:
    if opcao == 1:
        print("Seu numero em binario é {}".format(bin(numero)[2:])) #Caso queira pegar o resultado depois do "0b" print("Seu numero em binario é {}".format(bin(numero)[2:]))
    elif opcao == 2:
        print("Seu numero em octal é {}".format(oct(numero)[2:])) #Caso queira pegar o resultado depois do "0o" print("Seu numero em octal é {}".format(oct(numero)[2:]))
    else:
        print(f"Seu numero em hexadecimal é {hex(numero)[2:]}") #Caso queira pegar o resultado depois do "0x"  print(f"Seu numero em hexadecimal é {hex(numero)[2:]}")


