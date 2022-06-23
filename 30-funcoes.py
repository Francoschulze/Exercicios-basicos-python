"""
Faça um programa para imprimir:
    1
    2 2
    3 3 3
    ........
n n n n n n n n...n
para um N informado pelo usuário. Use uma função que receba um valor n
inteiro e imprima até a N-ésima linha.

"""


def esboco(n):
    # O primieor laço for será com o número de linhas
    for linha in range(1, n + 1):
        # Agora que estamos dentro das linhas, repetimos a quantidade dela
        for coluna in range(linha):
            # \t é utilizado para exibir 4 espaçoes
            # end='' mostra o que você quer ver no final da string.
            # No nosso caso a não quebra de linha.
            print(f'\t{linha}', end='')
        print()


def exibe():
    n = int(input('Valor de N: '))
    esboco(n)


while True:
    exibe()

