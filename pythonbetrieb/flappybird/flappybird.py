# imports
import random
import pygame
import time
import os

# find path
path = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# colors
BLACK=(0,0,0)
WHITE=(255, 255, 255)
RED=(255,0,0)
GREEN=(0, 255, 0)

# variables
width=1900
hight=1000
fps=240
a=1000
b=0
c=0
d=0
e=0
f=0
cx=0
xmultiplier=1400/width
ymultiplier=700/hight
pipex1=width
pipex2=width+(width/2)
birdy=hight/2 
score_player=0
status=-1
xfive=0
yfive=0
gotfive=1
notfive=1
soundoff=0
soundeffoff=0
skin=0
clickedx=0
clickedy=0
newhighscore=0
enter=0
nametext=""
done = False

# screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([width, hight])
pygame.display.set_caption("Flappybird")

# fonts
font = pygame.font.Font('freesansbold.ttf', 50)
font1 = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 100)

# files
jump=pygame.mixer.Sound("jump.mp3")
point=pygame.mixer.Sound("point.mp3") 
die=pygame.mixer.Sound("die.mp3")
fivepoint=pygame.mixer.Sound("fivepoints.wav")
backgroundmusic=pygame.mixer.music.load("song.mp3")
backgroundmusic=pygame.mixer.music.play(-1,-10.0)
bird_image=pygame.image.load("flappybird.png")
bird_image.set_colorkey(WHITE)
bird = bird_image.get_rect()
bird_image1=pygame.image.load("flappybird1.png")
bird_image1.set_colorkey(WHITE)
bird_image2=pygame.image.load("flappybird2.png")
bird_image2.set_colorkey(WHITE)
bird_image3=pygame.image.load("flappybird3.png")
bird_image3.set_colorkey(WHITE)
pipeb_image=pygame.image.load("pipeb.png")
pipeb_image.set_colorkey(WHITE)
pipe1b= pipeb_image.get_rect()
pipe2b= pipeb_image.get_rect()
pipet_image=pygame.image.load("pipet.png")
pipet_image.set_colorkey(WHITE)
pipe1t= pipet_image.get_rect()
pipe2t= pipet_image.get_rect()
five=pygame.image.load("five.jpg")
settings=pygame.image.load("settings.png")
sound=pygame.image.load("sound.png")
sound.set_colorkey(WHITE)
sky=pygame.image.load("sky.png")
skysize= pygame.transform.scale(sky, (width,hight))

# definitions
def prescreen():
    global clickedx,clickedy,status
    text = font2.render("Flappybird", True, BLACK)
    text1 = font.render("This game is about controlling a bird ", True, BLACK)
    text2 = font.render("and trying to fly between green pipes", True, BLACK)
    text3 = font.render("without touching them.", True, BLACK)
    text4 = font.render("Press ENTER to start", True, BLACK)
    text5 = font.render("or press H to view the highscores.", True, BLACK)
    screen.blit(text,  [width/2-250, hight/2-200])
    screen.blit(text1, [width/2-425, hight/2-75])
    screen.blit(text2, [width/2-425, hight/2-25])
    screen.blit(text3, [width/2-270, hight/2+25])
    screen.blit(text4, [width/2-250, hight/2+125])
    screen.blit(text5, [width/2-390, hight/2+175])
    screen.blit(settings,(width/2+400,hight/2-195))
    if width/2+400<clickedx<width/2+475 and hight/2-195<clickedy<hight/2-120:
        status=3

def showhighscore():
    global status
    file = open("names.txt")
    for line in file:
        namelist=line.split(",")
    file.close()
    for i in range(1,6):
        names = font.render(str(i)+". " + namelist[-i]+":", True, BLACK)
        screen.blit(names, [width/2-175,hight/2-200+(50*i)])
    file = open("highscore.txt")
    for line in file:
        highscorelist=line.split(",")
    file.close()
    for i in range(1,6):
        highscores = font.render(highscorelist[-i], True, BLACK)
        screen.blit(highscores, [width/2+175,hight/2-200+(50*i)])
    pygame.draw.rect(screen, GREEN, [width/2-175, hight/2+175, 380, 100])
    text = font.render("Back to lobby", True, BLACK)
    screen.blit(text, [width/2-150, hight/2+200])
    if width/2-175<clickedx<width/2+205 and hight/2+175<clickedy<hight/2+275:
        status=-1

def endscreen():
    global status, newhighscore,enter
    text1 = font.render("or press ESCAPE to exit.", True, BLACK)
    text2 = font.render("Your score was: " + str(score_player), True,BLACK)
    text4 = font.render("Back to lobby", True, BLACK)
    screen.blit(text1, [width/2-300, hight/2+300])
    screen.blit(text2, [width/2-250, hight/2-200])
    pygame.draw.rect(screen, GREEN, [width/2-200, hight/2+175, 380, 100])
    screen.blit(text4, [width/2-180, hight/2+200])
    if width/2-200<clickedx<width/2+185 and hight/2+175<clickedy<hight/2+275:
        status=-1
        newhighscore=0   
        enter=0 

def settingsscreen():
    global fps,soundoff,cx,soundeffoff,status,skin
    text = font.render("Settings", True, BLACK)
    text1 = font.render("FPS:", True, BLACK)
    text2 = font.render("60", True, RED)
    text3 = font.render("144", True, RED)
    text4 = font.render("240", True, RED)
    text5 = font.render("Backgroundmusik:", True, BLACK)
    text6 = font.render("Soundeffects:", True, BLACK)
    text8 = font.render("Skin:", True, BLACK)
    text7 = font.render("Back to lobby", True, BLACK)
    screen.blit(text,[width/2-100, hight/2-300])
    screen.blit(text1, [width/2-300, hight/2-200])
    pygame.draw.rect(screen, GREEN, [width/2-150, hight/2-200, 100, 50])
    pygame.draw.rect(screen, GREEN, [width/2, hight/2-200, 100, 50])
    pygame.draw.rect(screen, GREEN, [width/2+150, hight/2-200, 100, 50])
    screen.blit(text2, [width/2-130, hight/2-200])
    screen.blit(text3, [width/2+5, hight/2-200])
    screen.blit(text4, [width/2+155, hight/2-200])
    if width/2-150<clickedx<width/2-50 and hight/2-200<clickedy<hight/2-150:
        fps=60
        pygame.draw.rect(screen, RED, [width/2-150, hight/2-200, 100, 50])
        text2 = font.render("60", True, GREEN)
        screen.blit(text2, [width/2-130, hight/2-200])
    if width/2<clickedx<width/2+100 and hight/2-200<clickedy<hight/2-150:
        fps=144
        pygame.draw.rect(screen, RED, [width/2, hight/2-200, 100, 50])
        text3 = font.render("144", True, GREEN)
        screen.blit(text3, [width/2+5, hight/2-200])
    if width/2+150<clickedx<width/2+250 and hight/2-200<clickedy<hight/2-150:
        fps=240
        pygame.draw.rect(screen, RED, [width/2+150, hight/2-200, 100, 50])
        text4 = font.render("240", True, GREEN)
        screen.blit(text4, [width/2+155, hight/2-200])
    screen.blit(text5, [width/2-300, hight/2-100])
    screen.blit(sound, (width/2+200,hight/2-100))
    if width/2+200<clickedx<width/2+250 and hight/2-100<clickedy<hight/2-50 and cx!=clickedx:
        cx=clickedx
        if soundoff==0:
            soundoff=1 
            pygame.mixer.music.pause() 
        else:
            soundoff=0
            pygame.mixer.music.unpause()
    if soundoff==1:
        pygame.draw.line(screen,RED,(width/2+200,hight/2-50),(width/2+250,hight/2-100),5)
    screen.blit(text6, [width/2-300, hight/2])
    screen.blit(sound, (width/2+200,hight/2))
    if width/2+200<clickedx<width/2+250 and hight/2<clickedy<hight/2+50 and cx!=clickedx:
        cx=clickedx
        if soundeffoff==0:
            soundeffoff=1 
        else:
            soundeffoff=0
    if soundeffoff==1:
        pygame.draw.line(screen,RED,(width/2+200,hight/2+50),(width/2+250,hight/2),5)
    screen.blit(text8,[width/2-300, hight/2+100])
    pygame.draw.rect(screen, GREEN, [width/2-107, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2-7, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2+93, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2+193, hight/2+93, 65, 50])
    if width/2-107<clickedx<width/2-42 and hight/2+93<clickedy<hight/2+143:
        skin=0
        pygame.draw.rect(screen, RED, [width/2-107, hight/2+93, 65, 50])
    if width/2-7<clickedx<width/2+58 and hight/2+93<clickedy<hight/2+143:
        skin=1
        pygame.draw.rect(screen, RED, [width/2-7, hight/2+93, 65, 50])
    if width/2+93<clickedx<width/2+158 and hight/2+93<clickedy<hight/2+143:
        skin=2
        pygame.draw.rect(screen, RED, [width/2+93, hight/2+93, 65, 50])
    if width/2+193<clickedx<width/2+258 and hight/2+93<clickedy<hight/2+143:
        skin=3
        pygame.draw.rect(screen, RED, [width/2+193, hight/2+93, 65, 50])
    screen.blit(bird_image,( width/2-100,hight/2+100))
    screen.blit(bird_image1,( width/2,hight/2+100))
    screen.blit(bird_image2,( width/2+100,hight/2+100))
    screen.blit(bird_image3,( width/2+200,hight/2+100))
    pygame.draw.rect(screen, GREEN, [width/2-175, hight/2+175, 380, 100])
    screen.blit(text7, [width/2-150, hight/2+200])
    if width/2-175<clickedx<width/2+205 and hight/2+175<clickedy<hight/2+275:
        status=-1

def birdmovement():
    global birdy, a
    if a<(20*fpsmultiplier):
        birdy-=(5.25/fpsmultiplier)/ymultiplier
        a+=1
    else:
        birdy+=(4.5/fpsmultiplier)/ymultiplier
    if birdy<=0:
        birdy=0.1
    elif birdy>=hight-36:
        birdy=(hight-36.1)

def pipemovement():
    global pipex1,pipex2,b,c,pipey1,pipey2,e
    if score_player<=99:
        pipex1-=(6.25/fpsmultiplier)/xmultiplier
        pipex2-=(6.25/fpsmultiplier)/xmultiplier
    elif score_player>99:
        pipex1-=(7.5/fpsmultiplier)/xmultiplier
        pipex2-=(7.5/fpsmultiplier)/xmultiplier
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
    if score_player>=199:
        if e<=120*fpsmultiplier:
            pipey1+=0.025*fpsmultiplier
            pipey2-=0.025*fpsmultiplier
            e+=1
        elif 120*fpsmultiplier<e<=240*fpsmultiplier:
            pipey1-=0.025*fpsmultiplier
            pipey2+=0.025*fpsmultiplier
            e+=1
        elif e>240*fpsmultiplier:
            e=0

def plusfive():
    global yfive,xfive,gotfive,notfive,clickedx,clickedy,yfive,score_player,f
    if xfive<-82:
        notfive=1
    if clickedx>0:
        if xfive<=clickedx<=xfive+81 and yfive<=clickedy<=yfive+50:
            gotfive=1 
            score_player+=5
            if soundeffoff==0:
                fivepoint.play()
    clickedx=0
    clickedy=0
    if gotfive==1 or notfive==1:
        spawnfive=random.randrange(5,10)
        yfive=random.randrange(0,hight-50)
        xfive=random.randrange(width*(spawnfive/2)+50,width*(spawnfive/2)+width/2-81,50)
        gotfive=0
        notfive=0
    else:
        if score_player<=99:
            xfive-=(6.25/fpsmultiplier)/xmultiplier
        else:    
            xfive-=(7.5/fpsmultiplier)/xmultiplier
    if score_player>=199:
        if f<=60*fpsmultiplier:
            yfive+=0.05*fpsmultiplier
            f+=1
        elif 60*fpsmultiplier<f<=120*fpsmultiplier:
            yfive-=0.05*fpsmultiplier
            f+=1
        elif f>120*fpsmultiplier:
            f=0

def blititems():
    global skin
    if skin==0:
        screen.blit(bird_image,( 100,birdy))
    elif skin==1:
        screen.blit(bird_image1,( 100,birdy))
    elif skin==2:
        screen.blit(bird_image2,( 100,birdy))
    elif skin==3:
        screen.blit(bird_image3,( 100,birdy))
    screen.blit(pipeb_image,( pipex1,pipey1+200))
    screen.blit(pipeb_image,( pipex2,pipey2+200))
    screen.blit(pipet_image,( pipex1,-1000+pipey1))
    screen.blit(pipet_image,( pipex2,-1000+pipey2))
    screen.blit(five,(xfive,yfive))

def collisioncheck():
    global status,score_player
    bird.x = 100
    bird.y = birdy
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
        if soundeffoff==0:
            die.play()
        status=1
    else:
        if 50-(6.25/fpsmultiplier)/xmultiplier<=pipex1<=50 or 50-(6.25/fpsmultiplier)/xmultiplier<=pipex2<=50:
            score_player+=1
            if soundeffoff==0:
                point.play()

def updatefps():
    fps= str(int(clock.get_fps()))
    fpstext = font1.render(fps, 1, RED)
    screen.blit(fpstext, (width-50,10))

def showscore(): 
    global score_player
    score = font.render("Score: " + str(score_player), True, BLACK)
    screen.blit(score,(20,20))

def updatehighscore():
    global newhighscore,img,cursor,rect,enter
    file = open("highscore.txt")
    for line in file:
        highscore_list=line.split(",")
    file.close()
    g = int(score_player)
    if g >= int(highscore_list[-1]):
        newhighscore+=1
        if newhighscore==1:
            file = open("highscore.txt",'a')
            file.write(",")
            file.write(str(g))
            file.close()
        text=font.render("Just type your name:", True, BLACK)
        screen.blit(text, [width/2-425, hight/2-100])
        img = font.render(nametext, True, RED)
        rect = img.get_rect()
        rect.topleft = (width/2+100,hight/2-100)
        cursor = pygame.Rect(rect.topright, (3, rect.height))
        screen.blit(img, (width/2+100,hight/2-100))
        text1 = font.render(("Press ENTER to save your name."), True,BLACK)
        screen.blit(text1, [width/2-425, hight/2])
        rect.size=img.get_size()
        cursor.topleft = rect.topright
        if time.time() % 1 > 0.5 and enter ==0:
            pygame.draw.rect(screen, RED, cursor)
    text3 = font.render("The Highscore is: " + highscore_list[-1], True, BLACK)
    screen.blit(text3, [width/2-280, hight/2-150])
    

# main programm loop
while not done:

# userinputs 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                mouse=pygame.mouse.get_pos()
                clickedx=mouse[0]
                clickedy=mouse[1]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_h and (status==-1):
                status=2
            elif event.key == pygame.K_RETURN and (status==-1):
                status = 0
                birdy=hight/2 
                score_player=0
                pipex1=width
                pipex2=width+(width/2)
            elif event.key == pygame.K_SPACE and status==0 and d==0:
                a = 0
                d=1
                if soundeffoff==0:
                    jump.play()
            elif newhighscore>0:
                if event.key == pygame.K_BACKSPACE and enter!=1:
                    if len(nametext)>0:
                        nametext = nametext[:-1]
                elif event.key == pygame.K_RETURN and enter!=1:
                    file = open("names.txt",'a')
                    file.write(",")
                    file.write(nametext)
                    file.close()
                    enter=1
                else:
                    if enter!=1:
                        nametext += event.unicode
                img = font.render(nametext, True, RED)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and status==0:
                d=0
                
# background
    screen.blit(skysize,(0,0))

# pre game lobby
    if status==-1:
        prescreen()

# running game
    elif status==0:
        plusfive()
        pipemovement()
        birdmovement()
        collisioncheck()
        showscore() 
        blititems()
        
# game over
    elif status==1:
        updatehighscore()
        endscreen()

# highscore screen
    elif status==2:
        showhighscore()

# settings
    elif status==3:
        settingsscreen()

# update screen
    fpsmultiplier=fps/60
    clock.tick(fps)
    updatefps()
    pygame.display.flip()

# bye
pygame.quit()