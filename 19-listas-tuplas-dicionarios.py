"""
Escreva um programa que some todos os elementos de uma lista.
"""

# lista = [1, 2, 3, 4, 5, 6, 10, 15, 13]
# Utilizando a função sum()
# print(f'A soma dos itens na lista é = {sum(lista)} ')


lista = [1, 12, 22, 4, 5, 6, 10, 10, 13]

soma = 0

for i in lista:
    soma += i

print(f'Soma da lista: {soma} ')
