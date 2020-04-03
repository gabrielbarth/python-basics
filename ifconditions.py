# coding: utf-8

alto = False
magro = True
vegano = False

if alto:
  print("Você é alto.")
else:
  print("Você não é alto")

# Em python, ao invés de utilizar os operadores && para 'e' e || para 'ou',
# utiliza-se 'and' para o operador 'e' e 'or' para o operador 'ou'.

# Em python, 'elif' equivale ao 'else if' de outras linguagens

if magro and vegano:
  print("Você é magro e vegano")
elif magro and not(vegano):
  print("Você é magro, mas não é vegano")
elif not(magro) and vegano:
  print("Você não é magro, mas é vegano")
else:
  print("Você não é magro nem vegado")