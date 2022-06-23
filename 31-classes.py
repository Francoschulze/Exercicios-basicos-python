"""
Crie um método de saque, onde só deve ser possível fazer um saque
se a pessoa tiver um saldo positivo, e o saque máximo é esse valor.
O programa deve exibir um looping infinito, perguntando se a pessoa desejar
depositar ou sacar valores.
"""
from time import sleep


class Conta:
    saldo = 0.0

    def __init__(self):
        print('Conta Corrente criada! ')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('Não é possível depositar valor menor do que zero. ')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print(f'Valor insuficiente para saque. Seu saldo é {self.saldo} ')

    def exibir_saldo(self):
        return self.saldo


cliente = Conta()

opcao = True

while opcao:
    print('0. Sair;\n'
          '1. Exibir saldo;\n'
          '2. Depositar;\n'
          '3. Sacar;\n')
    opcao = int(input('Digite sua opção:\n '))
    if opcao == 1:
        print(f'Saldo da sua conta: {cliente.exibir_saldo():.2f}\n ')
    elif opcao == 2:
        deposito = float(input('Digite o valor a ser depositado:\n '))
        print(f'Valor depositado R$ {deposito:.2f}\n')
        cliente.depositar(deposito)
    elif opcao == 3:
        saque = float(input('Digite o valor para saque:\n '))
        print(f'Saque efetuado R$ {saque:.2f}\n ')
        cliente.sacar(saque)
    else:
        print('saindo do sistema... ')
        sleep(3)
