import os,time,random, json
from datetime import datetime

def limparTela():
    os.system('cls')

def aguardar(tempo):
    time.sleep(tempo)

def inicializarBancoDeDados():
    try:
        banco = open("base.atitus", "r")
    except:
        print("Banco de dados não encontrado, criando um novo...")
        banco = open("base.atitus", "w")

def escreverDados(nome, pontos):
    banco = open("base.atitus", "r")
    dados = banco.read()
    banco.close()

    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

        data_atual = datetime.now().strftime("%d/%m/%Y")
        dadosDict[nome] = (pontos, data_atual)

        banco.open("base.atitus", "w")
        banco.write(json.dumps(dadosDict))
        banco.close()

def maiorPontuador():
    banco = open("base.atitus", "r")
    dados = banco.read()
    banco.close()

    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    nome_maior = None
    dataJogada =  None
    maior_pontos = -1

    for nome, info in dadosDict.items():

        pontos = info[0]
        
        if pontos > maior_pontos:
            maior_pontos = pontos
            nome_maior = nome
            dataJogada = info[1]            

    return nome_maior, maior_pontos, dataJogada
