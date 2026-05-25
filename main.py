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
imagem = pygame.image.load("bases/fundoRua.png")
imagem2 = pygame.image.load("bases/fundoRua.png")
fundo = pygame.transform.scale(imagem, tamanho)
fundo2 = pygame.transform.scale(imagem2, tamanho)
fps = pygame.time.Clock()


def start():

    posicaoXFundo = 0
    posicaoYFundo = 0

    posicaoXFundo2 = 1000
    posicaoYFundo2 = 0

    bola_pos = (500, 350)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
