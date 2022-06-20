"""
Escreva um programa que solicite o nome, o sobrenome e o salário atual
de um funcionário e que calcule seu novo salário considerando cenários
hipotéticos, com os seguintes aumentos: 10%, 25%, 30% e 50%. A
mensagem de retorno deverá seguir o seguinte padrão
    "Olá, [nome] [sobrenome]"
    "Seu salário atual é : [salário]"
    "Seu salário com 10% de aumento é: [salário]"
    "Seu salário com 25% de aumento é: [salário]"
    "Seu salário com 30% de aumento é: [salário]"
    "Seu salário com 50% de aumento é: [salário]"

    Dica: No campo nome e sobrenome utilize os métodos strip() e title().
          O primeiro método permite remover os espaços antes e após a string,
          enquanto que o último permite colocar a string no formato titlecased
          (capitaliza string).
"""

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
salario_atual = float(input('Digite seu salário atual: '))

# Utilizamos o \n para que o código faça a quebra de linha.
print(f'Olá, {nome} {sobrenome}!\n'
      f'Seu salário atual é: R$ {salario_atual:.2f}\n'
      f'Seu salário com 10% de aumento será: R$ {salario_atual * 1.1:.2f}\n'
      f'Seu salário com 25% de aumento será: R$ {salario_atual * 1.25:.2f}\n'
      f'Seu salário com 30% de aumento será: R$ {salario_atual * 1.3:.2f}\n'
      f'Seu salário com 50% de aumento será: R$ {salario_atual * 1.5:.2f}\n')
