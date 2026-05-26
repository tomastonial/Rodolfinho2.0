import os,time,random, pygame
from recursos.funcoes import *

limparTela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maiorPontuador()
pygame.init()

# while True:
#     nome = input("NICKNAME: ")
#     if len(nome) > 0:
#         break
#     else:
#         print("O nickname deve conter pelo menos 1 caractere.")
    
tamanho = (1000, 700)
pygame.display.set_caption("RODOLFO")

relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
branco = (255,255,255)
preto = (0,0,0)
imagem = pygame.image.load("bases/Rua.jpg")
imagem = pygame.transform.rotate(imagem, 90)
imagem2 = pygame.image.load("bases/Rua.jpg")
imagem2 = pygame.transform.rotate(imagem2, 90)
fundo = pygame.transform.scale(imagem, tamanho)
fundo2 = pygame.transform.scale(imagem2, tamanho)
carroAzul = pygame.image.load("bases/CarroB.png")
carroAzul = pygame.transform.scale(carroAzul, (100, 137.5))
carroAzulD = pygame.transform.rotate(carroAzul, 90)
carroAzulE = pygame.transform.rotate(carroAzul, -90)
carroVermelho = pygame.image.load("bases/CarroR.png")
carroVermelho = pygame.transform.scale(carroVermelho, (100, 137.5))
carroVermelhoD = pygame.transform.rotate(carroVermelho, 90)
carroVermelhoE = pygame.transform.rotate(carroVermelho, -90)
carroVerde = pygame.image.load("bases/CarroG.png")
carroVerde = pygame.transform.scale(carroVerde, (100, 137.5))
carroVerdeD = pygame.transform.rotate(carroVerde, 90)
carroVerdeE = pygame.transform.rotate(carroVerde, -90)
cachorro = pygame.image.load("bases/cachorrosemfundo.png")
cachorro = pygame.transform.rotate(cachorro, -90)
fps = pygame.time.Clock()


def start():

    posicaoXFundo = 0
    posicaoYFundo = 0

    posicaoXFundo2 = 1000
    posicaoYFundo2 = 0

    yDogFaixa1 = 80
    yDogFaixa2 = 220
    yDogFaixa3 = 360
    yDogFaixa4 = 500

    yMovDog = 140

    xDog = 500
    # yDog = 143.75 # Faixa 1
    # yDog = 212.5 # Meio da Faixa de cima
    yDog = 220 # Faixa 2
    # yDog = 350 # Meio da Faixa do meio
    # yDog = 418.75 # Faixa 3
    # yDog = 487.5 # Meio da Faixa de baixo
    # yDog = 556.25 # Faixa 4
    # Faixa 1 para carros -> 95
    # Faixa 2 para carros -> 235
    # Faixa 3 para carros -> 365
    # Faixa 4 para carros -> 505
    faixas = [95, 235, 365, 505]
    yCarroB = random.choice(faixas)
    yCarroR = random.choice(faixas)
    yCarroG = random.choice(faixas)
    xCarroB = 0
    xCarroR = 0
    xCarroG = 0
    # Posiçao inicial dos carros
    if yCarroB == 95 or yCarroB == 235:
        xCarroB = 1000
    else:
        xCarroB = 0
    if yCarroR == 95 or yCarroR == 235:
        xCarroR = 1000
    else:
        xCarroR = 0
    if yCarroG == 95 or yCarroG == 235:
        xCarroG = 1000  
    else:
        xCarroG = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                if yDog <= yDogFaixa1:
                    yDog = yDogFaixa1
                else:
                    yDog -= yMovDog
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                if yDog >= yDogFaixa4:
                    yDog = yDogFaixa4
                else:
                    yDog += yMovDog
        Dog_pos = (xDog, yDog)
        tela.fill(branco)
        tela.blit(fundo, (posicaoXFundo, posicaoYFundo))
        tela.blit(fundo2, (posicaoXFundo2, posicaoYFundo2))
        posicaoXFundo -= 1
        posicaoXFundo2 -= 1
        if posicaoXFundo <= -1000:
            posicaoXFundo = 1000
        if posicaoXFundo2 <= -1000:
            posicaoXFundo2 = 1000
        # Movimento do carro azul

        tela.blit(cachorro, (Dog_pos))
        if yCarroB == 95 or yCarroB == 235:
            tela.blit(carroAzulE, (xCarroB, yCarroB))
            xCarroB -= 2
        else:
            tela.blit(carroAzulD, (xCarroB, yCarroB))
            xCarroB += 2
        if xCarroB < -200 or xCarroB > 1200:

            yCarroB = random.choice(faixas)

            if yCarroB in [95, 235]:
                xCarroB = 1000
            else:
                xCarroB = -100
        # Movimento do carro vermelho
        if yCarroR == 95 or yCarroR == 235:
            tela.blit(carroVermelhoE, (xCarroR, yCarroR))
            xCarroR -= 3
        else:
            tela.blit(carroVermelhoD, (xCarroR, yCarroR))
            xCarroR += 3
        if xCarroR < -200 or xCarroR > 1200:

            yCarroR = random.choice(faixas)

            if yCarroR in [95, 235]:
                xCarroR = 1000
            else:
                xCarroR = -100
        # Movimento do carro verde
        if yCarroG == 95 or yCarroG == 235:
            tela.blit(carroVerdeE, (xCarroG, yCarroG))
            xCarroG -= 4
        else:
            tela.blit(carroVerdeD, (xCarroG, yCarroG))
            xCarroG += 4
        if xCarroG < -200 or xCarroG > 1200:

            yCarroG = random.choice(faixas)

            if yCarroG in [95, 235]:
                xCarroG = 1000
            else:
                xCarroG = -100
        fps.tick(120)   
        pygame.display.update()

start()
