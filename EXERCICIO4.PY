#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 4) Ler quatro valores referentes a quatro notas escolares
# de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado,
# se o valor da média escolar for maior ou igual a 7. 
# Se o valor da média for menor que 7, solicitar a nota de exame,
# somar com o valor da média e obter nova média. Se a nova média for maior ou igual a 5,
# apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi aprovado,
# indicar uma mensagem informando esta condição. 
# Apresentar com as mensagens o valor da média do aluno, para qualquer condição.

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
if media>=7:
    print("O aluno foi aprovado com média", media)
else:
    nota_exame=float(input("Digite a nota do exame: "))
    nova_media=(media+nota_exame)/2
    if nova_media>=5:
        print("O aluno foi aprovado em exame com nova média", nova_media)
    else:
        print("O aluno não foi aprovado com nova média", nova_media)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")