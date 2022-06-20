"""
Escreva um programa que calcule o Índice de Massa Corporal (IMC),
utilizado para mensurar o peso ideal de uma pessoa. Dados de entrada:
nome, idade, peso e altura do usuário. O resultado do IMC deve ser
calculado e classificado de acordo com as seguintes regras:
"""
#        IMC:                             DESCRIÇÃO:
#     IMC   <        17             Muito abaixo do peso ideal
#     17    <= IMC < 18,5           Abaixo do peso
#     18,5 <= IMC < 25             Peso normal
#     25    <= IMC < 30             Acima do peso
#     30    <= IMC < 35             Obesidade I
#     35    <= IMC < 40             Obesidade II
#     IMC   >=       40             Obesidade III (mórbida)

# Fórmula:
# IMC = Massa/Altura²

nome = input('Digite seu nome: ').strip().title()
idade = input('Digite sua idade: ').strip()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

if imc < 17:
    print(f'Peso: {peso}\n'
          f'IMC: {imc:.2f}\n'
          f'Muito abaixo do seu peso ideal!')
elif 17 <= imc < 18.5:
    print(f'Seu peso: {peso}\n'
          f'Seu IMC: {imc:.2f}\n'
          f'Abaixo do peso!')
elif 18.25 <= imc < 25:
    print(f'Seu peso: {peso}\n'
          f'Seu IMC: {imc:.2f}\n'
          f'Peso normal!')
elif 25 <= imc < 30:
    print(f'Seu peso: {peso}\n'
          f'Seu IMC: {imc:.2f}\n'
          f'Acima do peso!')
elif 30 <= imc < 35:
    print(f'Seu peso: {peso}\n'
          f'Seu IMC: {imc:.2f}\n'
          f'Obesidade I!')
elif 35 <= imc < 40:
    print(f'Seu peso: {peso}\n'
          f'Seu IMC: {imc:.2f}\n'
          f'Obesidade II')
else:
    print('Obesidade III (mórbida)')