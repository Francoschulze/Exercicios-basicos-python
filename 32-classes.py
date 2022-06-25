# Passando os parâmetros diretamente no construtor da classes
#
# class Carro:
#     def __init__(self, modelo, portas):
#         # self.portas refere-se ao atributo
#         # portas refere-se ao argumento
#         self.portas = portas
#         self.modelo = modelo
#         print(f'{modelo} criado! Ele tem {self.portas} portas. ')
#
#
# palio = Carro('Palio', 2)

"""
Cara ou Coroa com Orientação a Objetos
"""
# Importando os módulos random e time
import random
from time import sleep


# Criando a classe cara ou coroa
class CaraCoroa:
    # Método construtor da classe
    # Iniciamos como se o lado da moeda virado para cima seja CARA
    def __init__(self):
        self.lado = 'Cara'

    # Criando o método lançar moeda
    def lancar(self):
        # Se o método randint gerar o número que dê 0 como resto da divisão
        if random.randint(0, 1) % 2 == 0:
            # O lado será definido como CARA
            # Utilizei o método upper.() para transformar toda a string em maiúscula
            self.lado = 'Cara'.upper()
            # Caso contrário será COROA
        else:
            self.lado = 'Coroa'.upper()
        return self.lado


# Instanciando a classe
moeda = CaraCoroa()

# utilizei o tratamento de excessão caso o usuário entre com o valor incorreto
try:
    # Aqui criamos um laço para que o jogador efetue os lançamentos.
    while True:
        op = int(input('0. Sair;\n'
                       '1. Lançar a moeda;\n'
                       'Digite sua opção: '))
        print()
        if op == 1:
            print(moeda.lancar())
            print()
        elif op == 0:
            print('Saindo do jogo...')
            sleep(3)
            break
        else:
            print('Opção inválida! ')
except ValueError:
    print('Erro de valor! ')
