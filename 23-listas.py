"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

numeros = []
par = []
impar = []

print('Informe 20 números:')

for i in range(20):
    numeros.append(int(input('Digite o número ' + str(i+1) + ':\n')))
    numero = numeros[i]

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'O números digitados foram {numeros}\n'
      f'Os números pares são: {par}\n'
      f'Os números ímpares são: {impar}')
