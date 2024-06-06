#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 2) Efetuar a leitura de um valor inteiro positivo
# ou negativo e apresentar o número lido como sendo um valor 
# positivo, ou seja, o programa deverá apresentar o módulo de
# um número fornecido. Lembre-se de verificar se o número 
# fornecido é menor que zero; sendo, multiplique-o por -1.

numero=int(input("Digite um valor inteiro: "))
if numero<0:
    numero=numero*-1  
print("O valor absoluto do número fornecido é:", numero)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")