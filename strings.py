# coding: utf-8

# Assim como em outras linguagens de progração, python conta com diversos métodos
# para manipulação de strings.
frase = "Frase teste"

# alguns métodos:

print(frase.upper())   # transforma as letrar em MAIÚSCULAS (FRASE TESTE)
print(frase.isupper()) # imprime True se as letras estiverem MAIÚSCULAS  (False)
print(frase.upper().isupper()) # transforma as letras em MAIÚSCULAS e verifica (True) 
print(frase[2]) # imprime a letra que está no index 2 ('a')
print(frase.index("a")) # imprime a posição em que letra encontra-se na string (2)
print(frase.index("tes")) # imprime a posição inicial do local onde há 'tes' na string (6)
print(frase.replace("Frase", "Texto")) # substitui 'Frase' por 'Texto' e imprime ("Texto teste")
