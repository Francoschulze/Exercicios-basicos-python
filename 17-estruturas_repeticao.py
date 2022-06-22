"""
Escreva um programa para somar todos os números naturais em um
intervalo definido pelo usuário.
"""

num = int(input('Digite um número natural: '))
intervalo = int(input('Digite o intervalo desejado: '))

soma = 0

for i in range(0, num + 1, intervalo):
    soma += i

print(f'Soma dos números com o intervalo de {intervalo} é = {soma} ')
