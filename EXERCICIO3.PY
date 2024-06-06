#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 3) Ler quatro valores referentes a quatro notas escolares
# de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, 
# se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado,
# indicar uma mensagem informando esta condição. Apresentar junto das mensagens
# o valor da média do aluno para qualquer condição.

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
if media>=5:
    print("O aluno foi aprovado com média", media)
else:
    print("O aluno não foi aprovado com média", media)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")