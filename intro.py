# coding: utf-8

# Este é um comentário em python. Basta utilizar '#' no início da linha.

'''
Este é um comentário com diversas linhas em Python.
Recomenda-se utilizar comentários com '#' ao invés deste.
'''

# Imprimindo na tela
# Para imprimir informações na tela, basta usar a função print():
print('Este texto está sendo impresso no terminal do VSCode.')

# Variáveis
# Python tem tipagem dinâmica e por convensão, usa-se '_' para separar variáveis
# com mais de uma palavra
nome_completo = "Gabriel Barth Silvério"     #variável do tipo string
idade = str(22)          #variárvel do tipo inteiro convertida para string
altura = str(1.84)       #variárvel do tip float convertida para string
print("Sou " + nome_completo + ", tenho " + idade + ' de idade e '  + altura + 
  'm de altra')

# acima utilizamos a função srt() para converter inteiro para string, pois
# print( permite imprimir apenas um determinado tipo de valor.

# Input
# Para pegar dados do usuário através do teclado, basta usar a função input()
nome = input("Digite seu nome: ")
# aqui estamos armazenando o valor que será digitado dentro da variável 'nome'
print("Hello " + nome)