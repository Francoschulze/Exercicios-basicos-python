"""
Crie um método de saque, onde só deve ser possível fazer um saque
se a pessoa tiver um saldo positivo, e o saque máximo é esse valor.
O programa deve exibir um looping infinito, perguntando se a pessoa desejar
depositar ou sacar valores.
"""
# Importando o módulo time para utilizarmos o método sleep
from time import sleep


# Criando a classe conta
class Conta:
    # Iniciando o saldo em 0
    saldo = 0.0

    # Método __init__() é o construtor
    def __init__(self):
        print('Conta Corrente criada! ')

    # Método para depósitos
    def depositar(self, valor):
        # Aceitaremos apenas valor maiores que 0
        if valor > 0:
            # A cada depósito o valor será somado ao saldo anterior
            self.saldo += valor
        else:
            print('Não é possível depositar valor menor do que zero. ')

    # Método para saque
    def sacar(self, valor):
        # Será aceito apenas os valores solicitados que não ultrapassem o saldo
        if valor <= self.saldo:
            # A cada saque o valor será subtraído do saldo anterior
            self.saldo -= valor
        else:
            print(f'Valor insuficiente para saque. Seu saldo é {self.saldo} ')

    # Enfim criamos um método para mostrar o saldo do cliente
    def exibir_saldo(self):
        return self.saldo


# Instanciando a classe
cliente = Conta()

opcao = True

# Aqui criamos um loop para o cliente informar o que deseja
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
