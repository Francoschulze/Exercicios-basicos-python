"""
Faça um programa que peça 3 números e informe o maior e o menor dentre eles.
"""


def maior(x, y, z):
    maximo = x
    if y > maximo:
        maximo = y
    if z > maximo:
        maximo = z
    return maximo


def menor(x, y, z):
    minimo = x
    if y < minimo:
        minimo = y
    if z < minimo:
        minimo = z
    return minimo


def menu():
    x = int(input('digite o primeiro número: '))
    y = int(input('digite o segundo número: '))
    z = int(input('digite o terceiro número: '))

    print(f'O maior número é: {maior(x, y, z)} ')
    print(f'O menor número é: {menor(x, y, z)} ')


while True:
    menu()
    print()
