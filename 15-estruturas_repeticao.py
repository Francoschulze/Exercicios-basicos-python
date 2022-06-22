"""
Escreva um programa para checar se um determinado número é primo ou
não. Obs: Um número primo pode ser dividido por apenas dois números:
ele mesmo e o número 1
"""

num = int(input('Digite um número: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'O número {num} não é primo! ')
            break
    else:
        print(f'O número {num} é primo! ')
