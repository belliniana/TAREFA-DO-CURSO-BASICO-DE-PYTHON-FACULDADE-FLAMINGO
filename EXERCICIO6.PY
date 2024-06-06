#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 6) Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa,
# apresentando com saída uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado como masculino,
# ou a mensagem "Ilma Sra.", para o sexo informado como feminino. Apresente também junto da mensagem 
# de saudação o nome previamente informado.

nome=input("Digite o nome da pessoa: ")
sexo=input("Digite o sexo da pessoa (M para masculino, F para feminino): ")
if sexo.upper()=='M':
    print("Ilmo Sr.", nome)
elif sexo.upper()=='F':
    print("Ilma Sra.", nome)
else:
    print("Sexo não reconhecido. Por favor, informe M para masculino ou F para feminino.")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")