from analises.analisesIMC import analisarIMC
from calculadoras.calculoIMC import calcularIMC

print("Sistema de calculadora")
nomePessoa = str(input("Escreva o seu nome e tecle ENTER: "))
alturaPessoa = float(input("Escreva a sua altura, usando ponto no lugar da vírgula e tecle ENTER: "))
pesoPessoa = float(input("Escreva o seu peso, usando ponto no lugar da vírgula e tecle ENTER:  "))

imc = calcularIMC(pesoPessoa, alturaPessoa)

analisarIMC(imc, nomePessoa)

