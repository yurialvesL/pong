import pygame


pygame.init()


window = pygame.display.set_mode([1280,720]) #tamanho da janela
title = pygame.display.set_caption('Pong') # tipo da janela

field= pygame.image.load('assets/field.png') #carregando a imagem de background

win= pygame.image.load('assets/win.png')



score_1= 0
score1_img =pygame.image.load('assets/score/0.png')
score_2 = 0
score2_img =pygame.image.load('assets/score/0.png')




player1= pygame.image.load('assets/player1.png')
player1_y= 310
player1_x = 50
player1_moveup =  False
player1_movedown =  False





player2= pygame.image.load('assets/player2.png')
player2_y= 310
player2_moveup =  False
player2_movedown =  False




ball = pygame.image.load('assets/ball.png')
ball_x = 617
ball_y = 337
ball_dir = -5
ball_dir_y = 1


def move_player():
    global player1_y
    if player1_moveup:
        player1_y-=5
    else:
        player1_y +=0

    if player1_movedown:
        player1_y+=5
    else:
        player1_y +=0

    if player1_y <= 0: #condicional para que o boneco não passe da tela
        player1_y = 0
    elif player1_y >=575:
        player1_y = 575

    print(player1_y)


def move_player2():
    global player2_y

    if player2_moveup:
        player2_y-=5
    else:
        player2_y +=0

    if player2_movedown:
        player2_y+=5
    else:
        player2_y +=0


    if player2_y <= 0: #condicional para que o boneco não passe da tela
        player2_y = 0
    elif player2_y >=575:
        player2_y = 575

def move_ball():
    global  ball_x
    global  ball_y
    global ball_dir
    global player2
    global ball_dir_y
    global score_1
    global score_2
    global score2_img
    global score1_img

    ball_x +=ball_dir
    ball_y += ball_dir_y


    if ball_x < 120: #condicional para colisão da bola com o player1
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1

    if ball_x > 1100:#condicional para colisão da bola com o player2
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 685:
        ball_dir_y*=-1
    elif ball_y <=0:
        ball_dir_y *=-1


    if ball_x <- 50: #aqui é pra quando a bola passa da tela
        ball_x = 617
        ball_y =337
        ball_dir_y*=-1
        ball_dir *= -1
        score_2+=1
        score2_img = pygame.image.load('assets/score/'+str(score_2)+'.png')


    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score_1 += 1
        score1_img = pygame.image.load('assets/score/'+str(score_1)+'.png')


def draw():
    if score_1 or score_2 < 9:
        window.blit(field, (0, 0))  # colocando ele na tela seguindo o eixo x e y
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500,50))
        window.blit(score2_img, (710,50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win,(300,330))

loop =True #variavel para deixar a tela aberta constantemente, se ela for igual a false a janela irá fechar

while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT: #condição que pega o evento de fechar a janela
            loop= False
        if events.type == pygame.KEYDOWN:#condições para movimento do player 1
            if events.key == pygame.K_w:
                player1_moveup = True
            elif events.key ==  pygame.K_s:
                player1_movedown =  True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            elif events.key == pygame.K_s:
                player1_movedown = False


        if events.type == pygame.KEYDOWN: #condições para movimento do player 2
            if events.key == pygame.K_UP:
                player2_moveup = True
            elif events.key == pygame.K_DOWN:
                player2_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                player2_moveup = False
            elif events.key == pygame.K_DOWN:
                player2_movedown = False




    draw()


    pygame.display.update()



