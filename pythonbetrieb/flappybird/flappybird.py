# imports
import random
import pygame
import os

# find path
path = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# initialize
pygame.init()
clock = pygame.time.Clock()

# colors
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
GREEN=(0, 255, 0)
RED=(255,0,0)

# fonts
font = pygame.font.Font('freesansbold.ttf', 50)
font1 = pygame.font.Font('freesansbold.ttf', 20)

# variables
width=1900
hight=1000
pipex1=width
pipex2=width+(width/2)
birdy=hight/2 
fps=1000
a=1000
b=0
c=0
score_player=0
status=-1
done = False

# files
jump=pygame.mixer.Sound("jump.mp3")
point=pygame.mixer.Sound("point.mp3") 
die=pygame.mixer.Sound("die.mp3")
backgroundmusic=pygame.mixer.music.load("song.mp3")
backgroundmusic=pygame.mixer.music.play(-1,-10.0)
bird_image=pygame.image.load("flappybird.png")
bird_image.set_colorkey(WHITE)
bird = bird_image.get_rect()
pipeb_image=pygame.image.load("pipeb.png")
pipeb_image.set_colorkey(WHITE)
pipe1b= pipeb_image.get_rect()
pipe2b= pipeb_image.get_rect()
pipet_image=pygame.image.load("pipet.png")
pipet_image.set_colorkey(WHITE)
pipe1t= pipet_image.get_rect()
pipe2t= pipet_image.get_rect()

# screen
screen = pygame.display.set_mode([width, hight])
pygame.display.set_caption("My Game")

# definitions
def pressedenter():
    global status,birdy,score_player,pipex1,pipex2
    status = 0
    birdy=hight/2 
    score_player=0
    pipex1=width
    pipex2=width+(width/2)

def prescreen():
    schrift = pygame.font.SysFont('freesansbold.ttf', 50, True, False)
    text = schrift.render("Press ENTER to start.", True, WHITE)
    screen.blit(text, [width/2-250, hight/2-25])

def endscreen():
    text = font.render("Press ENTER to restart", True, WHITE)
    text1 = font.render("or press ESCAPE to exit.", True, WHITE)
    text2 = font.render("Your score was: " + str(score_player), True,WHITE)
    screen.blit(text, [width/2-250, hight/2-100])
    screen.blit(text1, [width/2-250, hight/2-50])
    screen.blit(text2, [width/2-250, hight/2])
    screen.blit(text3, [width/2-250, hight/2+50])

def birdmovement():
    global birdy, a
    birdy+=hight*0.0004
    if a<150:
        birdy-=(hight*0.001333)
        a+=1
    if birdy<=0:
        birdy=0.1
    elif birdy>=hight-36:
        birdy=(hight-36.1)

def pipemovement():
    global pipex1,pipex2,b,c,pipey1,pipey2
    pipex1-=(width*0.0003)
    pipex2-=(width*0.0003)
    if pipex1<-50:
        pipex1=width
        b=0
    if pipex2<-50:
        pipex2=width
        c=0
    if b==0:
        pipey1=random.randrange(50,hight-200-50)
        b=1
    if c==0:
        pipey2=random.randrange(50,hight-200-50)
        c=1

def blititems():
    screen.blit(bird_image,( 100,birdy))
    screen.blit(pipeb_image,( pipex1,pipey1+200))
    screen.blit(pipeb_image,( pipex2,pipey2+200))
    screen.blit(pipet_image,( pipex1,-1000+pipey1))
    screen.blit(pipet_image,( pipex2,-1000+pipey2))

def collisioncheck():
    global status,score_player
    bird.x =100
    bird.y =birdy
    pipe1b.x =pipex1
    pipe1b.y =pipey1+200
    pipe2b.x =pipex2
    pipe2b.y =pipey2+200
    pipe1t.x =pipex1
    pipe1t.y =-1000+pipey1
    pipe2t.x =pipex2
    pipe2t.y =-1000+pipey2
    collide1 = bird.colliderect(pipe1b)
    collide2 = bird.colliderect(pipe2b)
    collide3 = bird.colliderect(pipe1t)
    collide4 = bird.colliderect(pipe2t)
    if collide1==1 or collide2==1 or collide3==1 or collide4==1:
        die.play()
        status=1
    else:
        if 50-(width*0.0003)<=pipex1<=50 or 50-(width*0.0003)<=pipex2<=50:
            score_player+=1
            point.play()

def updatefps():
    fps= str(int(clock.get_fps()))
    fpstext = font1.render(fps, 1, RED)
    screen.blit(fpstext, (width-50,10))
    

def showscore(scoreofplayer): 
    score = font.render("Score: " + str(scoreofplayer), True, WHITE)
    screen.blit(score,(20,20))

def updatehighscore():
    global text3
    highscore_list=[0]
    file = open("highscore.txt")
    for line in file:
        line = line.strip()
        highscore_list.append(line)
    g = int(score_player)
    file.close()
    if g > int(highscore_list[-1]):
        file = open("highscore.txt",'w')
        file.write(str(g))
    file.close()
    text3 = font.render("The Highscore is: " + highscore_list[-1], True, WHITE)   

# main programm loop
while not done:
    
# userinputs 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RETURN and (status==-1 or status==1):
                pressedenter()
            elif event.key == pygame.K_KP_ENTER and (status==-1 or status==1):
                pressedenter()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and status==0:
                a = 0
                jump.play()

    screen.fill(BLUE)
    if status==-1:
        prescreen()

# running game
    elif status==0:
        pipemovement()
        birdmovement()
        collisioncheck()
        showscore(score_player) 
        blititems()

# game over
    elif status==1:
        updatehighscore()
        endscreen()

    clock.tick(fps)
    updatefps()
    pygame.display.flip()
pygame.quit()