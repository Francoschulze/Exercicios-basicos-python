"""
Faça um Programa que leia uma lista de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
"""

letras = []
numero_consoantes = 0
consoantes = []
print('Informe os caracteres: ')
for i in range(10):
    letras.append((input('Caracter  ' + str(i+1) + ':\n')))
    letra = letras[i]
    if letra not in ('a', 'e', 'i', 'o', 'u'):
        numero_consoantes += 1
        consoantes.append(letra)

print(f'O total de consoantes digitadas foram: {numero_consoantes}.')
print(f'As consoantes digitadas foram: {consoantes}.')
