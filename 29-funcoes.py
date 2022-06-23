"""
Um número é dito perfeito quando ele é igual a soma de seus fatores. Por
exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2
e por 3) e a soma é equivalente ao número 6 (6 = 1 + 2 + 3), logo 6 é um número perfeito.
Escreva uma função que receba um inteiro e diz se é perfeito ou não. Em outra função, peça um
inteiro N e mostre todos os números perfeitos até N.

"""

# Teste o código abaixo com os seguintes valores:
# 28, 496, e 8128


# Essa função vai verificar se o número digitado é perfeito
def perfeito(n):
    soma = 0
    for valor in range(1, n):
        if n % valor == 0:
            soma += valor
    # Se a a soma dos antecessores for igual ao número digitado
    # Ele é perfeito
    if soma == n:
        return True
    # Caso contrário, não é.
    else:
        return False


# Essa função exibirá o(s) números perfeitos.
def exibe():
    # Solicitando a entrada
    n = int(input('Exibir perfeitos até o número: '))

    # Laço for para iterar todos os números perfeitos
    # Antecessores que retornaram True para exibi-los
    for valor in range(1, n+1):
        if perfeito(valor):
            print(f'{valor} é um número perfeito! ')


# Laço while para exibir até que você queira finaliza-lo
while True:
    exibe()
    print()
    sair = input('Para sair, digite [exit]: ')
    if sair == 'exit':
        break

    # A palavra reservada (continue) diz ao python para continuar o loop.
    else:
        continue
