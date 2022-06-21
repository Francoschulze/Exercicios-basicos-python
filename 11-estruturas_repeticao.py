"""
Escreva um programa que peça, indefinidamente, números reais (float) ao
usuário. Caso o número digitado não esteja situado entre 0 e 10 o programa
deverá ser finalizado, mostrando a soma e a quantidade de números digitados.
"""

# solicitamos o número ao usuário
numero = float(input('Digite um número entre 0 e 10: '))

# iniciamos a variável soma em 0, bem como o contador.
soma = 0
contador = 0

# O laço consiste no seguinte:
# Enquanto o número for menor ou igual a 10
# O número digitado será somado e o contador receberá o número 1
# Até o número digitado for maior que 10
while numero <= 10:
    soma += numero
    contador += 1
    numero = float(input('Digite um número entre 0 e 10: '))

print(f'Soma: {soma + numero:.2f}\n'
      f'Quantidade de números: {contador + 1}')
