"""
Faça um programa que converta o valor de grau Celsius para Fahrenheit.
"""


def celsius_para_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f


def fahrenheit_para_celsius(f):
    c = (f - 32) * 5 / 9
    return c


def menu():
    while True:
        opcao = int(input('1. Digite 1 para converter de grau CELSIUS para FAHRENHEIT: \n'
                          '2. Digite 2 para converter de grau FAHRENHEIT para CELSIUS: \n'
                          '3. Digite 3 caso queira sair: '))
        if opcao == 1:
            c = int(input('Digite a temperatura em graus celsius: '))
            print(f'Convertido para: {celsius_para_fahrenheit(c):.0f}° ')
        elif opcao == 2:
            f = int(input('Digite a temperatura em graus Fahrenheit: '))
            print(f'Convertido para: {fahrenheit_para_celsius(f):.0f}° ')
        elif opcao == 3:
            print('Espero que tenha gostado! ')
            break
        else:
            print('Opção inválida! ')


print(menu())
