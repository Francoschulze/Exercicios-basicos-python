"""
Escreva um programa que gere 100 números reais aleatórios, entre 0 e 1, e
armazene-os em uma lista. Ao final deve ser retornado as seguintes informações:
    a. Maior número;
    b. Menor número;
    c. Soma de todos os números gerados;
"""
# Para utilizarmos o módulo random devemos importar ele antes
from random import random

# Lista vazia que será preenchida conforme o laço for estiver sendo executado
lista = []

for i in range(1, 101):
    # Aqui utilizamos o método append para adicionar
    # Os elementos dentro da lista que está vazia
    # E a função random que vai gerar números entre 0 e 1.
    lista.append(random())

# Função max() retorna o valor máximo gerado na lista
print(f'Maior número: {max(lista)} ')
# Função min() retorna o valor mínimo gerado na lista
print(f'Menor número: {min(lista)} ')
# Função sum() retorna a soma de todos os itens gerados na lista.
print(f'Soma dos números gerados na lista: {sum(lista)} ')
