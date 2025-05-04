
#Pense em um código em Python com duas funções. Uma função para calcular a área de um quadrado e outra função para calcular a área de um retângulo.
#Escreva o código no ambiente de programação em python, salve em um arquivo chamado “figuras_geometricas.py” e execute o programa.
#Envie o arquivo  “figuras_geometricas.py” como resposta desta atividade.

def area_de_um_quadrado(lado):
  return lado * lado

def area_de_um_retangulo(base, atulra):
  return base * altura

lado = float(input("Digite o lado do quadrado: "))
print(f"Área do quadrado: {area_de_um_quadrado(lado)}")

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
print(f"Área do retângulo: {area_de_um_retangulo(base, altura)}")