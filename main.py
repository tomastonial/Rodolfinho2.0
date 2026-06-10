import os,time,random, pygame, pyttsx3, cx_Freeze
from recursos.trabalho import *

limparTela()
inicializarBancoDeDados()
nick_maior, maior_pontos, dataJogada = maiorPontuador()
pygame.init()

nick = pegarNick()
    
tamanho = (1000, 700)
pygame.display.set_caption("RODOLFO")
tela = pygame.display.set_mode(tamanho)
fonte = pygame.font.SysFont("Arial", 30)
fontePontos = pygame.font.SysFont("Arial", 30)
relogio = pygame.time.Clock()
branco = (255,255,255)
preto = (0,0,0)
imagem = pygame.image.load("bases/Rua.jpg")
imagem = pygame.transform.rotate(imagem, 90)
imagem2 = pygame.image.load("bases/Rua.jpg")
imagem2 = pygame.transform.rotate(imagem2, 90)
fundo = pygame.transform.scale(imagem, tamanho)
fundo2 = pygame.transform.scale(imagem2, tamanho)
img_pause = pygame.image.load("bases/imagem_pause.png")
img_inicio = pygame.image.load("bases/imagem_inicio.png")
img_derrota = pygame.image.load("bases/imagem_derrota.png")
img_derrota = pygame.transform.scale(img_derrota, tamanho)
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
frasePause = fonte.render("PRESS SPACE TO PAUSE", True, branco)
fraseResume = fonte.render("PRESSIONE SPACE PARA VOLTAR", True, branco)
maiorPontuadorTexto = fonte.render(f"MAIOR PONTUADOR: \n {nick_maior} \n {maior_pontos} pontos \n {dataJogada}", True, branco)
rodando = True
pausado = False
osso = pygame.image.load("bases/osso.png").convert_alpha()
tamanhoOsso = 50
crescendo = True
som = pygame.mixer.Sound("bases/som.mp3")
choro = pygame.mixer.Sound("bases/cachorro chorando.mp3")

pombo = pygame.image.load("bases/pombo.png")
pombo = pygame.transform.scale(pombo, (50, 70))
pomboE = pygame.transform.rotate(pombo, 90)
pomboD = pygame.transform.rotate(pombo, -90)

fps = pygame.time.Clock()
pontos = 0


def inicio():
    tela.blit(img_inicio, (0,0))
    tela.blit(maiorPontuadorTexto, (400, 550))
    pygame.display.update()

    startButton = pygame.Rect(378, 348, 254, 60)
    maiorButton = pygame.Rect(378, 428, 254, 60)

    mouse_pos = pygame.mouse.get_pos()

    if (startButton.collidepoint(mouse_pos)
        or maiorButton.collidepoint(mouse_pos)):

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if startButton.collidepoint(evento.pos):
                start()
            elif maiorButton.collidepoint(evento.pos):
                maiorPontuador()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        elif evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            




def pause():
    tela.blit(img_pause, (0,0))
    tela.blit(fraseResume, (320, 650))
    pygame.display.update()


def start():
    global pontos
    global tamanhoOsso
    global crescendo
    global osso
    ultimo_ponto = pygame.time.get_ticks()
    
    som.set_volume(0.5)
    som.play(-1)

    pontos = 0
    frasePontos = fonte.render(f"PONTOS: {pontos}", True, branco)

    tamanhoOsso = 50
    crescendo = True

    posicaoXFundo = 0
    posicaoYFundo = 0

    posicaoXFundo2 = 1000
    posicaoYFundo2 = 0

    velocidadeFundo = 1
    velocidadeCarroAzul = 2
    velocidadeCarroVermelho = 3
    velocidadeCarroVerde = 4
    velocidadePombo = 8


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
    # Pombo
    yPombo = posicaoPomboY()
    xPombo = direcaoPombo()

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
        agora = pygame.time.get_ticks()
        if agora - ultimo_ponto >= 1000:
            pontos += 1
            frasePontos = fonte.render(f"PONTOS: {pontos}", True, branco)
            ultimo_ponto = agora
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
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = True
                pause()
                while pausado:
                    som.stop()
                    for evento in pygame.event.get():
                        if  evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                            pausado = False
                            som.play(-1)
                        elif evento.type == pygame.QUIT:
                            pygame.quit()
                            quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()


        Dog_pos = (xDog, yDog)
        tela.fill(branco)
        tela.blit(fundo, (posicaoXFundo, posicaoYFundo))
        tela.blit(fundo2, (posicaoXFundo2, posicaoYFundo2))
        tela.blit(frasePontos, (10, 10))
        tela.blit(frasePause, (350, 650))
        tela.blit(osso, (900, 20))
        posicaoXFundo -= velocidadeFundo
        posicaoXFundo2 -= velocidadeFundo
        if posicaoXFundo <= -1000:
            posicaoXFundo = 1000
        if posicaoXFundo2 <= -1000:
            posicaoXFundo2 = 1000

        # Movimento do carro azul

        tela.blit(cachorro, (Dog_pos))
        if yCarroB == 95 or yCarroB == 235:
            tela.blit(carroAzulE, (xCarroB, yCarroB))
            xCarroB -= velocidadeCarroAzul
        else:
            tela.blit(carroAzulD, (xCarroB, yCarroB))
            xCarroB += velocidadeCarroAzul
        if xCarroB < -200 or xCarroB > 1200:

            yCarroB = random.choice(faixas)

            if yCarroB in [95, 235]:
                xCarroB = 1000
            else:
                xCarroB = -100

        # Movimento do carro vermelho
        if yCarroR == 95 or yCarroR == 235:
            tela.blit(carroVermelhoE, (xCarroR, yCarroR))
            xCarroR -= velocidadeCarroVermelho
        else:
            tela.blit(carroVermelhoD, (xCarroR, yCarroR))
            xCarroR += velocidadeCarroVermelho
        if xCarroR < -200 or xCarroR > 1200:

            yCarroR = random.choice(faixas)

            if yCarroR in [95, 235]:
                xCarroR = 1000
            else:
                xCarroR = -100
        # Movimento do carro verde
        if yCarroG == 95 or yCarroG == 235:
            tela.blit(carroVerdeE, (xCarroG, yCarroG))
            xCarroG -= velocidadeCarroVerde
        else:
            tela.blit(carroVerdeD, (xCarroG, yCarroG))
            xCarroG += velocidadeCarroVerde
        if xCarroG < -200 or xCarroG > 1200:

            yCarroG = random.choice(faixas)

            if yCarroG in [95, 235]:
                xCarroG = 1000
            else:
                xCarroG = -100
        # Movimento do pombo

        if xPombo >= -80 and xPombo <= 999:
            tela.blit(pomboD, (xPombo, yPombo))
            xPombo += velocidadePombo
            if xPombo >= 1000:
                yPombo = posicaoPomboY()
                xPombo = direcaoPombo()
        else:
            tela.blit(pomboE, (xPombo, yPombo))
            xPombo -= velocidadePombo
            if xPombo <= -80:
                yPombo = posicaoPomboY()
                xPombo = direcaoPombo()
        print(f"Pombo: ({xPombo}, {yPombo})")
        
        hitBoxDog = pygame.Rect(xDog, yDog, 100, 137.5)
        hitBoxCarroB = pygame.Rect(xCarroB, yCarroB, 100, 60)
        hitBoxCarroR = pygame.Rect(xCarroR, yCarroR, 100, 60)
        hitBoxCarroG = pygame.Rect(xCarroG, yCarroG, 100, 60)
        # Faz o osso crescer
        if crescendo:
            tamanhoOsso += 0.2

            if tamanhoOsso >= 60:
                crescendo = False

        # Faz o osso diminuir
        else:
            tamanhoOsso -= 0.2

            if tamanhoOsso <= 50:
                crescendo = True

        # Redimensiona a imagem do osso
        osso = pygame.transform.scale(
            osso,
            (int(tamanhoOsso), int(tamanhoOsso))
        )

        # Mantém o osso centralizado no canto
        xOsso = 925 - tamanhoOsso / 2
        yOsso = 45 - tamanhoOsso / 2

        morte = pygame.Rect.colliderect(hitBoxDog, hitBoxCarroB) or pygame.Rect.colliderect(hitBoxDog, hitBoxCarroR) or pygame.Rect.colliderect(hitBoxDog, hitBoxCarroG)
        if morte:
            print("Morreu")
            som.stop()
            choro.play()
            rodando = False
            perdeu()
            break
        fps.tick(120)   
        pygame.display.update()

def perdeu():
    escreverDados(nick, pontos)
    print("VOCÊ PERDEU!")

    playAgainButton = pygame.Rect(516, 550, 225, 85)
    homeButton = pygame.Rect(257, 550, 225, 85)

    pygame.event.clear()
    while True:
        tela.blit(img_derrota, (0,0))
        frasePontosMorte = fontePontos.render(f"PONTOS: {pontos}", True, branco)
        tela.blit(frasePontosMorte, (420, 490))
        tela.blit(maiorPontuadorTexto, (10, 530))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if playAgainButton.collidepoint(evento.pos):
                    choro.stop()
                    start()
                    return
                elif homeButton.collidepoint(evento.pos):
                    choro.stop()
                    inicio()
                    return

        fps.tick(60)
        

if nick != None:
    while rodando:
        inicio()
    else:
        perdeu()
