# -*- coding: utf-8 -*-
"""Oficina 04 - Estruturas de Repetição e Estrutura de Dados
"""

#Crie um programa que use um laço for para imprimir os números de 1 a 5 no console.
for n in range(1,6):
  print(n)

#Escreva um programa que declare uma lista com os números [10, 20, 30, 40, 50] e exiba o primeiro elemento.
Lista = [10, 20, 30, 40, 50]
print(Lista[0])

#Faça um programa que use um laço while para somar todos os números de 1 a 10 e exiba o resultado no console.
n = 1
soma = 0

while n <= 10:
    soma += n
    n += 1

print(soma)

#Crie um programa que declare um dicionário com as seguintes chaves e valores: {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"} e exiba o valor associado à chave "idade"
dicionario = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
print(dicionario["idade"])

#Escreva um programa que inverta uma string utilizando um laço for. Por exemplo, para a string "Python", o resultado deve ser "nohtyP".
string = "Python"

inverte = ""

for letra in string:
    inverte = letra + inverte

print(inverte)

#Escreva um programa que calcule a frequência de cada caractere em uma string. Por exemplo, na string "banana", o programa deve exibir: {'b': 1, 'a': 3, 'n': 2}
string = "banana"
frequencia = {}

for letra in string:
    if letra in frequencia:
        frequencia[letra] += 1
    else:
        frequencia[letra] = 1

print(frequencia)