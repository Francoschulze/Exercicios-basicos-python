"""
Escreva um programa que peça uma string ao usuário e retorne na tela a
quantidade de caracteres da string. Dica: use a função built-in len() e trate
a string com o método strip().
"""

caracteres = input('Digite alguma coisa: ').strip()

print(f'Você digitou: {caracteres}')
print(len(caracteres))
