"""
Faça um programa que calcule a média e a soma de 3 números digitados
"""


def soma(x, y, z):
    return x + y + z


def media(num):
    return num / 3


def menu():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    z = float(input('Terceiro número: '))

    print(f'Soma = {soma(x, y, z):.2f}')
    print(f'Media = {media(soma(x, y, z)):.2f}')


# While é opcional
# Apenas para o programa continuar rodando.
while True:
    menu()
    print()
