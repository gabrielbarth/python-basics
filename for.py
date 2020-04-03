

# -*- coding: utf-8 -*-

A = input()
B = input()



print("X = " + A + B)

for letra in "Frase para teste":
  print(letra)

pessoas = ["Kleber", "Marcos", "Junior"]
for p in pessoas:
  print(p)


# imprime os valores de 3 a 9
for index in range(3, 10):
  print(index)

# função que recebe dois parâmetros (base, potencia)
def elevar_potencia (base_num, pot_num):
  result = 1
  for index in range(pot_num):
    result = result * base_num
  return result


print(elevar_potencia(3, 2)) 
# chama a função passando dois parâmetros e imprime o retorno