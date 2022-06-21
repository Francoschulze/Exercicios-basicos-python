"""
Escreva um programa que receba 3 números do usuário e retorne na tela o
maior número digitado.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior digitado!')
elif n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior digitado!')
else:
    print(f'O número {n3} é o maior digitador!')
