#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 1) Ler dois valores numéricos inteiros e apresentar o 
# resultado da diferença do maior pelo menor valor.

valor1=int(input("Digite o primeiro valor inteiro: "))
valor2=int(input("Digite o segundo valor inteiro: "))
if valor1>valor2:
    maior_valor=valor1
    menor_valor=valor2
else:
    maior_valor=valor2
    menor_valor=valor1
diferenca=maior_valor-menor_valor
print("A diferença entre o maior e o menor valor é:", diferenca)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")