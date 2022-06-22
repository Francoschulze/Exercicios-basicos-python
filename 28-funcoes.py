"""
A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um
script em Python que simule 1 milhão de lançamentos de dados e mostre a
frequência que deu para cada número
"""
import random


def gerador():
    return random.randint(1, 6)


def repeticao(n):
    teste1 = teste2 = teste3 = teste4 = teste5 = teste6 = 0
    for valor in range(n):
        teste = gerador()

        if teste == 1:
            teste1 += 1
        elif teste == 2:
            teste2 += 1
        elif teste == 3:
            teste3 += 1
        elif teste == 4:
            teste4 += 1
        elif teste == 5:
            teste5 += 1
        elif teste == 6:
            teste6 += 1
    print(f'O número 1 saiu: {teste1} vezes = {(teste1 / n) * 100:.0f}% ')
    print(f'O número 2 saiu: {teste2} vezes = {(teste2 / n) * 100:.0f}% ')
    print(f'O número 3 saiu: {teste3} vezes = {(teste3 / n) * 100:.0f}% ')
    print(f'O número 4 saiu: {teste4} vezes = {(teste4 / n) * 100:.0f}% ')
    print(f'O número 5 saiu: {teste5} vezes = {(teste5 / n) * 100:.0f}% ')
    print(f'O número 6 saiu: {teste6} vezes = {(teste6 / n) * 100:.0f}% ')


def menu():
    n = int(input('Quantos lançamentos de dado você deseja: '))
    repeticao(n)


while True:
    menu()
    print()
