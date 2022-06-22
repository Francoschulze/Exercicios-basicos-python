"""
Escreva um programa para imprimir a sequência de Fibonacci até o
n-ésimo termo definido pelo usuário. Certifique que o usuário digite um
número inteiro positivo.
Obs: Fibonacci é uma sequência de números inteiros, começando por 0 e 1,
na qual cada termo subsequente corresponde à soma dos dois anteriores.
Os primeiros 10 números da sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
"""

num = int(input('Digite um número para visualizar a sequência de Fibonacci: '))

# Os dois primeiros termos não sofrem alteração
termo_1, termo_2 = 0, 1
contador = 0

# verificando se o número é positivo
if num <= 0:
    print('O número não pode ser negativo! ')

# Se o número digitado for igual 1, o primeiro termo será mostrado na tela
elif num == 1:
    print(termo_1)

# Senão o código faz o looping para calcular a sequência
# Caso queira visualizar melhor, coloque um break e rode o debug
else:
    pass
    while contador < num:
        print(termo_1, end=' ')
        termo_1, termo_2 = termo_2, termo_1 + termo_2
        contador += 1
