# tradutor que troca qualquer vogal para a letra 'g'

def translate(frase):
  traducao = ""
  for letra in frase:
    if letra.lower() in 'aeiou':
      if letra.isupper():
        traducao = traducao + "G"
      else:
        traducao = traducao + "g"
    
    else:
      traducao = traducao + letra
  
  return traducao

print(translate(input("Entre com uma frase: ")))