#exercicio 1
def inicio():
    anoNascimento = int (input('Digite o ano de seu nascimento: '))
    idade = int (2024 - anoNascimento)

    print("sua idade em 2024 era provavelmente: ",idade, " anos\n")


#exercicio 2
def inicio():
    valorBase = float(input('Digite o valor da base do retângulo: '))
    valorAltura = float(input('Digite o valor da altura do retangulo: '))

    if valorAltura > 0 and valorBase > 0:
        valorArea = valorBase * valorAltura
        print("O valor da área é: ",valorArea," metros quadrados")

    else:
        print('O valor dos lados de um retângulo não podem ser negativos...')


#exercicio 3

#colocar aplicacao antes da funcao inicio
def soma(n1,n2):
    print(n1 + n2)

def sub(n1,n2):
    print(n1 - n2)

def mult(n1,n2):
    print(n1 * n2)

def divi(n1,n2):
   if n2 != 0:
        print(n1 / n2)
   else:
        print('Nao eh posssivel realizar uma divisao por zero!...')

def inicio():
#identacao
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    print("Que tipo de operação voce deseja realizar: \n")
    escolha = (int(input("1| soma\n2| Subtracao\n3| multiplicacaon\n4| divisao\n")))

    if escolha == 1:
     soma(num1,num2)

    elif escolha == 2:
        sub(num1,num2)

    elif escolha == 3:
        mult(num1,num2)

    elif escolha == 4:
        divi(num1,num2)

    else:
        print("Opção inválida.")

#chamada funcao inicio
inicio()


#exercicio 4

def avaliar(num):
    if num > 0:
        print("Positivo")
    else:
        print("Negativo")

def inicio():
    num = float(input('Digite um numero: '))

    avaliar(num)

inicio()


#exercicio 5

def avaliacao(nota):
    if nota >=7:
        print("Aprovado")
        if nota == 10:
            print("Parabens pelo esforco")
    else:
        print("Reprovado")

def inicio():
    nota = float(input("Informe a nota que voce tirou na prova: "))
    avaliacao(nota)

inicio()


#exercicio 6

def idadeAvaliar(idade):
    if idade >= 18:
        print("Voce eh maior de idade")
    else:
        print("Voce eh menor de idade")

def inicio():
    idade = int(input("Informe sua idade: "))
    idadeAvaliar(idade)

inicio()


#exercicio 7

def aplicacaoAumento(salario):
    if salario <= 1000:
        salario += salario * 0.10
        print("Aumento aplicado de 10%: R$ ", salario)
    elif salario > 1000:
        salario += salario * 0.05
        print("Aumento aplicado de 5%: R$ ", salario)

def inicio():
    salario = float(input("Informe seu salario: "))
    aplicacaoAumento(salario)

inicio()


#exercicio 8

def desconto(custo):
    if custo >= 50:
        custo -= custo * 0.15
        print("Desconto aplicado de 15%: R$ ", custo)
    else:
        print("Nao foi possivel aplicar desconto ao produto: R$ ", custo)

def inicio():
    custo = float(input('Informe o custo do produto: '))
    desconto(custo)

inicio()


#exercicio 9

def lerVelocidade(velocidade):
    if velocidade >= 80.0:
        print('Veiculo multado')
    else:
        print('Velocidade inferior a 80 km/h, nao multado')

def inicio():
    velocidade = float(input('Informe a velocidade do veiculo (em km/h): '))
    lerVelocidade(velocidade)

inicio()


#exercicio 10

def convercao(temperaturaC):
    temperaturaF = (temperaturaC * 9 / 5)+32
    print(temperaturaF,"° Farenheit")

def inicio():
    temperaturaC = int(input('Informe a temperatura em Celsius: °'))
    convercao(temperaturaC)

inicio()
