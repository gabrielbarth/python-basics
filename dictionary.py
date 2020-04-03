# coding: utf-8

'''
Em Python dictionário é uma coleção não ordenada de valores de dados, 
usada para armazenar valores de dados como um mapa. O Dictionary mantém um par 
chave: valor. O valor da chave é fornecido no dicionário para torná-lo mais 
otimizado.
'''

ConversaoMeses = {
  "Jan": "Janeiro",
  "Fev": "Fevereiro",
  "Mar": "Março",
  "Abr": "Abril",
  "Mai": "Maio",
  "Jun": "Junho",
  "Jul": "Julho",
  "Ago": "Agosto",
  "Set": "Setembro",
  "Out": "Outubro",
  "Nov": "Novembro",
  "Dez": "Dezembro",
}

print(ConversaoMeses["Nov"]) # imprime o valor atribuido àquela chave
print(ConversaoMeses.get("Ago")) # também podemos acessar através de um método get
print(ConversaoMeses.get("Xis", "Valor inválido.")) 
# podemos também retornar uma mensagem quando a chave for inválida