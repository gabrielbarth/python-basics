# coding: utf-8

i = 1
while i <= 10:
  print(i)
  i += 1

print('Loop finalizado!')

palavra_secreta = "xis-beico"
palavra_entrata = "" 
entrada_cont = 0
entrada_limite = 5
limite_extrapolado = False


while palavra_secreta != palavra_entrata and not(limite_extrapolado):
  if entrada_cont < entrada_limite:
    palavra_entrata = input("Digite a palava_secreta: ")
    entrada_cont += 1
  else:
    limite_extrapolado = True

if limite_extrapolado:
  print("Você perdeu, limite de entradas estourado!")
else:
  print("Você venceu!")