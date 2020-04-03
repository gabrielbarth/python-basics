# coding: utf-8

# Python pode ser classificada como uma lp dinamicamente tipada,
# logo podemos fazer coisas do tipo:

print(2)
print(2.45)
print(2 + 5.5)
print(10 % 3)
print(-2.987435)
print("---------------------------------")


# Assim como em outras linguagens de progração, python conta com diversos métodos
# para manipulação de números também.

meu_numero = -5
print(abs(meu_numero)) # imprime o valor absoluto (5)

print(pow(3, 2)) # eleva um numero a uma potência (9)
print(max(40, 6, 90, 25)) # imprime o maior valor (90)
print(min(40, 6, 90, 25)) # imprime o menor valor (6)
print(round(3.2)) # imprime o valor arredondado (3)
print(round(3.7)) # imprime o valor arredondado (4)

from math import *   # impotando a bliblioteca de matemática do python
# Convencionalmente, as importações devem vim no topo do código (lá em cima!) 
print(floor(3.7)) # imprime o valor arredondando-o para o inteiro subsequente
print(ceil(3.2)) # imprime o valor arredondando-o para o inteiro consequente
print(sqrt(36)) # imprime a raiz quadrada