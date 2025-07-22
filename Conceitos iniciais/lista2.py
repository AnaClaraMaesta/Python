#desafio 1

def inicio():
    distanciaViagem = float(input('Qual a distancia da viagem? (em km): '))
    velocidadeMedia = float(input('Qual a velocidade media esperada? (em km/h): '))
    consumoCarro = float(input('Qual o consumo do carro? (em km/l): '))
    percoCombustivel = float(input('Qual o preço médio do combustível?: R$'))
    orcamento = float(input('Qual o orcamento?: R$'))

    tempoEstimado(distanciaViagem, velocidadeMedia)
    custo = totalViagem(distanciaViagem, consumoCarro, percoCombustivel)

    if custo > orcamento:
        print('ATENCAO: o custo da viagem ultrapassa o orcamento!')
    else:
        print('O custo da viagem esta dentro do orcamento')

def tempoEstimado (distanciaViagem, velocidadeMedia):
    tempo = distanciaViagem / velocidadeMedia

    if tempo >= 5:
        print('A viagem será de ',tempo,' horas\n')
        print('Alerta de viagem longa, planeje paradas...')
    else:
        print('A viagem será de ',tempo,'horas\n')

def totalViagem(distanciaViagem, consumoCarro, precoMedio):
    litrosNecessarios  = distanciaViagem / consumoCarro
    custoTotal = litrosNecessarios * precoMedio

    return custoTotal

inicio()


#desafio 2

def inicio():
    consumoMensal = float(input('Qual o consumo do mensal de energia? (em kWh): '))
    quantidadePessoas = int(input('Qual a quantidade de pessoas na residencia?: '))

    consumoPessoa = consumoPorPessoa(consumoMensal, quantidadePessoas)
    totalCusto = precoTotal(consumoMensal)

    if consumoMensal <= 100:
        print('Voce recebeu um desconto de 15%, o valor a pagar sera: R$',totalCusto - totalCusto * 0.15,'\n')
    elif consumoMensal >=300 :
        print('Pelo consumo superar 300kwh você recebeu uma taxa de 50 reais, o valor da sua conta foi: R$ ',totalCusto + 50,'\n')
    elif consumoMensal in range(100,299.9):
        print('O valor a pagar sera: R$ ',totalCusto,'\n')
    else:
        print('Algo deu errado...')

def consumoPorPessoa(consumoMensal, quantidadePessoas):
    consumoPessoa = consumoMensal / quantidadePessoas

    if consumoPessoa < 50:
        print('Sua classificação de consumo é: Econômico!')
        if consumoPessoa < 50 and consumoMensal < 200:
            print('\nVocê recebeu um bônus de R$ 20,00 por economia!')
    elif consumoPessoa >= 50:
        print('Sua classificação de consumo é: Moderada')
    elif consumoPessoa >= 100:
        print('Sua classificação de consumo é: Alto Consumo')

    return consumoPessoa
def precoTotal (consumoMensal):
    precoTotal = consumoMensal * 0.50
    return precoTotal

inicio()