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
fps = pygame.time.Clock()


def start():

    posicaoXFundo = 0
    posicaoYFundo = 0

    posicaoXFundo2 = 1000
    posicaoYFundo2 = 0

    xBola = 500
    yBola = 143.75 # Faixa 1
    yBola = 212.5 # Meio da Faixa de cima
    yBola = 281.25 # Faixa 2
    yBola = 350 # Meio da Faixa do meio
    yBola = 418.75 # Faixa 3
    yBola = 487.5 # Meio da Faixa de baixo
    yBola = 556.25 # Faixa 4
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                if yBola == 143.75:
                    yBola = 143.75
                else:
                    yBola -= 137.5
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                if yBola == 556.25:
                    yBola = 556.25
                else:
                    yBola += 137.5
        bola_pos = (xBola, yBola)
        tela.fill(branco)
        tela.blit(fundo, (posicaoXFundo, posicaoYFundo))
        tela.blit(fundo2, (posicaoXFundo2, posicaoYFundo2))
        posicaoXFundo -= 1
        posicaoXFundo2 -= 1
        if posicaoXFundo <= -1000:
            posicaoXFundo = 1000
        if posicaoXFundo2 <= -1000:
            posicaoXFundo2 = 1000
        pygame.draw.circle(tela, preto, bola_pos, 20)
        fps.tick(320)   
        pygame.display.update()

start()
