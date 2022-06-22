"""
Faça um programa que leia 4 notas, adicione-as dentro de uma lista
e mostre o cálculo da média.
"""

nota = []
media = 0

for i in range(4):
    nota.append(int(input('Digite 4 notas para o cálculo da média: ')))
    media += nota[i]

media = media / 4
print(f'Você digitou as notas: {nota} e a média foi: {media:.2f}.')
