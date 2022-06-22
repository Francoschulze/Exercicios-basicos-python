"""
Escreva um programa que dado um número inteiro positivo (N), pelo
usuário, calcule e retorne na tela:
a. A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;
b. A soma dos n primeiros números pares;
c. A soma dos n primeiros números ímpares.
"""

num = int(input('Digite um número inteiro: '))

contador = 0
soma = 0
soma_par = 0
soma_impar = 0

while contador < num:
    for i in range(1, num + 1):
        contador += 1
        soma += i
        if i % 2 == 0:
            soma_par += i
        elif i % 2 != 0:
            soma_impar += i

print(f'A soma dos N números inteiros antecessores é = {soma}. ')
print(f'A soma dos N números pares antecessores é = {soma_par}. ')
print(f'A soma dos N números ímpares antecessores é = {soma_impar}. ')
