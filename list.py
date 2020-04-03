# coding: utf-8

# Em python, chamamos um array/vetor de lista

pessoas = [ "Joana", "Gabriel", "Felipe", "Pedro", "Joana" ]

print(pessoas) # imprime a lista 'pessoas'
print(pessoas[1]) # imprime posição 2 da lista (Gabriel)
print(pessoas[-2]) # imprime posição 2 da lista inversa (Felipe)
print(pessoas[1:3]) # imprime as posições 1 a 2 da lista (Gabriel, Felipe)

# Funções de uma lista
numeros_aleatorios = [34, 23, 5, 16, 78]

pessoas.extend(numeros_aleatorios) # une números aleatórios ao final da lista 'pessaos'
print(pessoas) # imprime a nova lista 'pessoas'

pessoas.remove("Felipe") # remove 'Felipe' da lista
print(pessoas) # imprime a nova lista 'pessoas'
# pessoas.clear() # limpa a lista apagando todos seus valores
pessoas.pop() # remove o item de index -1 da lista (Pedro)

pessoas.insert(1, "Kelly") # insere 'Kelly na posição 1 da lista
print(pessoas.index("Gabriel")) # retorna a posição de 'Gabriel' na lista (2)
print(pessoas.count("Joana")) # retorna a quantidade de 'Joana' na lista
pessoas.sort() # ordena de forma crescente
print(pessoas)
pessoas.reverse() # ordena de forma decrescente
print(pessoas)

pessoas2 = pessoas[:] # gera uma cópia
print(pessoas2)
