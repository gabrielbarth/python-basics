# coding: utf-8

# Calculadora das quatro operações operações em python

num1 = float(input("Digite o primeiro número: "))
op = input("Digite o operador (+, -, / ou *): ")
num2 = float(input("Digite o segundo número: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
else :
  print(num1 * num2)