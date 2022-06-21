"""
Escreva um programa que peça um número inteiro do usuário e mostre na
tela o fatorial deste número. Obs: Não utilizar funções ou métodos de
bibliotecas.
"""
# 0! = 1 e 1! = 1
# n! = n . (n – 1). (n – 2). (n – 3) ... 2,1.

num = int(input('Digite um número inteiro: '))

# Iniciando os valores com 1 você elimina linhas de código
# Para identificar o valor de entrada de 0 e 1.
fatorial = 1
contador = 1

# Enquanto o contador for menor que o número de entrada
# Ele permanecerá fazendo o cálculo.
# Assim sendo, o fatorial é calculado.
while contador <= num:
    fatorial *= contador
    contador += 1

print(f'O fatorial do número {num} é = {fatorial}!')
