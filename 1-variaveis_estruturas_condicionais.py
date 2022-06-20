"""
Escreva um programa que calcule a área de uma circunferência.
O usuário deve digitar o valor do raio e o programa deverá retornar a área da
circunferência. Utilize a fórmula: A = pi * R², em que pi é uma constante e R o
raio da circunferência. Você pode usar a biblioteca math para utilizar o valor
da constante pi.

"""
from math import pi

# Raio
r = float(input('Digite o raio da circunferência: '))
print(f'Área: {pi * r ** 2:.2f}²')
