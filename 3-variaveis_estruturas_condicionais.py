"""
Escreva um programa para calcular a hipotenusa de um triângulo. Você
pode utilizar o módulo math (math.hypot). H² = (a² + b²)/2
"""

from math import hypot

# Primeiro pedimos os catetos

cateto_adjacente = float(input('Digite o cateto adjacente: '))
cateto_oposto = float(input('Digite o cateto oposto: '))

# Função hypot() já realiza o cálculo da hipotenusa.
# Você só precisa passar os argumentos.
# hipotenusa = hypot(cateto_adjacente, cateto_oposto)

print(f'Hipotenusa: {hypot(cateto_adjacente, cateto_oposto):.1f}')