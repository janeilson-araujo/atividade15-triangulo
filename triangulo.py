# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

print("descubra se um triângulo é possível ")
lado1 = float(input("digite o 1° lado do triângulo:"))
lado2 = float(input("digite o 2° lado do triângulo:"))
lado3 = float(input("digite o 3° lado do triângulo:"))

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    print("o triângulo é possível")
else:
    print("o triângulo não é possível ")