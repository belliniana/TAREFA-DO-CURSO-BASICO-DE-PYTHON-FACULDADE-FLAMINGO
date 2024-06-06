#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 5) Efetuar a leitura de três valores (variáveis A, B e C)
# e apresentá-los dispostos em ordem crescente.

A=float(input("Digite o valor de A: "))
B=float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
menor=A
if B<menor:
    menor=B
if C<menor:
    menor=C
maior=A
if B>maior:
    maior=B
if C>maior:
    maior=C
meio=(A+B+C)-menor-maior
print("Os valores em ordem crescente são:", menor, ",", meio, ",", maior)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")