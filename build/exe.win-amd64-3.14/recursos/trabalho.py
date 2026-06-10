import os,time,random, json, pygame
from datetime import datetime

def pegarNick():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 0 and len(nome) <= 20:
            return nome
        else:
            print("Nome inválido, tente novamente.")

def limparTela():
    os.system('cls')

def aguardar(tempo):
    time.sleep(tempo)

def posicaoPomboY():
    return random.randint(80, 500)

def direcaoPombo():
    posicoesPossiveis = [-80, 1000]
    return random.choice(posicoesPossiveis)

def inicializarBancoDeDados():
    try:
        banco = open("base.atitus", "r")
        print("Banco de dados encontrado!")
        aguardar(2)
    except:
        print("Banco de dados não encontrado, criando um novo...")
        aguardar(2)
        banco = open("base.atitus", "w")

def escreverDados(nick, pontos):
    with open("base.atitus", "r") as banco:
        dados = banco.read()

    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    data_atual = datetime.now().strftime("%d/%m/%Y")

    # Usuário não existe ainda
    if nick not in dadosDict:
        dadosDict[nick] = (pontos, data_atual)

    # Usuário existe, verifica se bateu o recorde
    elif pontos > dadosDict[nick][0]:
        dadosDict[nick] = (pontos, data_atual)

    with open("base.atitus", "w") as banco:
        banco.write(json.dumps(dadosDict))

def maiorPontuador():
    banco = open("base.atitus", "r")
    dados = banco.read()
    banco.close()

    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    nick_maior = None
    dataJogada =  None
    maior_pontos = -1

    for nick, info in dadosDict.items():

        pontos = info[0]
        
        if pontos > maior_pontos:
            maior_pontos = pontos
            nick_maior = nick
            dataJogada = info[1]            

    print(f"MAIOR PONTUADOR: {nick_maior} - {maior_pontos} pontos - {dataJogada}")
    return nick_maior, maior_pontos, dataJogada

