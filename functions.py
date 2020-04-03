# coding: utf-8

# Em python, as funções não necessitam de chaves para circundar o corpo, mas sim
# de identação:

# declarando uma função que imprime 'oi' na tela
def diga_oi():
  print("Oi")

diga_oi() # chamando a função

# declarando uma função que recebe dois parâmetros
def say_my_name(nome, idade):
  print("I am " + nome + " and I'm " + str(idade) + " years old.")

say_my_name("Heisenberg", 42) # chamando a função e passando dois parâmetros


# Funções com retorno

# declarando uma função que recebe um número retorna este ao cubo
def cubo(num):
  return num*num*num

print(cubo(3)) # chamando a função e passando um número como parâmetro




