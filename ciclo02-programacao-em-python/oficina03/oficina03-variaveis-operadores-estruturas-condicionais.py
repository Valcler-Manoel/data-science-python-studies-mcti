# -*- coding: utf-8 -*-
"""Oficina 03 - Variáveis, Operadores e Estruturas Condicionais
"""

# Crie um programa que verifique se o número 15 é maior que 10 e exiba "Sim" ou "Não" no console.

numero = 15
if numero > 10:
    print("Sim")
else:
    print("Não")


# Escreva um programa que use o operador ** para calcular 2³ e exiba o resultado.

calculo = 2 ** 3
print(calculo)


# Crie um programa que use o operador * para repetir a string "Oi!" cinco vezes.

string = "Oi!" * 5
print(string)


# Escreva um programa que calcule a média de três números inteiros 10, 20 e 30, e exiba no console se a média é maior, menor ou igual a 20.

n1 = 10
n2 = 20
n3 = 30

media = (n1 + nu2 + n3) / 3

if media > 20:
    print("A média é maior que 20")
elif media < 20:
    print("A média é menor que 20")
else:
    print("A média é igual a 20")


 #Crie um programa que determine se o número 45 é divisível por 3 e por 5 simultaneamente. O programa deve exibir "Divisível por 3 e 5" ou "Não é divisível .
 # Define o número a ser verificado

numero = 45

if numero % 3 == 0 and numero % 5 == 0:
    print("Divisível por 3 e 5")
else:
    print("Não é divisível")