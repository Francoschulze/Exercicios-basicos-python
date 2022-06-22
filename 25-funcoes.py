"""
Faça um programa que calcule a media de 3 notas digitadas
"""


def soma(num_1, num_2, num_3):
    return num_1 + num_2 + num_3


def media():
    num_1 = float(input('Digite o primeiro número: '))
    num_2 = float(input('Digite o segundo número: '))
    num_3 = float(input('Digite o terceiro número: '))
    resultado = soma(num_1, num_2, num_3)
    print(f'A média é = {resultado / 3:.2f} ')


media()
