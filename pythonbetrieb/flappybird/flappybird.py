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
width=1500  #Laptop:1500/Monitor:1900
hight=800   #Laptop:800/Monitor:1000
fps=240
jumpduration=1000
pipe1reset=0
pipe2reset=0
clickedspace=0
pipeupdown=0
fiveupdown=0
xmultiplier=1400/width
ymultiplier=700/hight
pipex1=width
pipex2=width+(width/2)
birdy=hight/2 
score_player=0
status=4
xfive=0
yfive=0
background1x=0
background2x=width
gotfive=1
notfive=1
soundoff=0
soundeffoff=0
skin=0
clickedx=0
clickedy=0
newhighscore=0
enter=0
text=""
done = False

# screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([width, hight])
pygame.display.set_caption("Flappybird")

# fonts
defaultfont = pygame.font.Font('freesansbold.ttf', 50)
fpssize = pygame.font.Font('freesansbold.ttf', 20)
headline = pygame.font.Font('freesansbold.ttf', 100)

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
customizedbird= pygame.transform.scale(bird_image, (400,282))
bird_image1=pygame.image.load("flappybird1.png")
bird_image1.set_colorkey(WHITE)
customizedbird1= pygame.transform.scale(bird_image1, (400,282))
bird_image2=pygame.image.load("flappybird2.png")
bird_image2.set_colorkey(WHITE)
customizedbird2= pygame.transform.scale(bird_image2, (400,282))
bird_image3=pygame.image.load("flappybird3.png")
bird_image3.set_colorkey(WHITE)
customizedbird3= pygame.transform.scale(bird_image3, (400,282))
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
info=pygame.image.load("info.png")
sky=pygame.image.load("sky.png")
customizedsky= pygame.transform.scale(sky, (width,hight+5))

# definitions
def prescreen():
    global clickedx,clickedy,status, skin
    screen.blit(headline.render("Flappybird", True, BLACK),  [width/2-250, hight/2-200])
    screen.blit(defaultfont.render("Press ENTER to start", True, BLACK), [width/2-250, hight/2+225])
    screen.blit(defaultfont.render("or press H to view the highscores.", True, BLACK), [width/2-390, hight/2+275])
    screen.blit(settings,(width/2+400,hight/2-195))
    screen.blit(info, (width/2-400,hight/2-195))
    if skin==0:
        screen.blit(customizedbird,(width/2-200,hight/2-75))
    elif skin==1:
        screen.blit(customizedbird1,(width/2-200,hight/2-75))
    elif skin==2:
        screen.blit(customizedbird2,(width/2-200,hight/2-75))
    elif skin==3:
        screen.blit(customizedbird3,(width/2-200,hight/2-75))
    if width/2+400<clickedx<width/2+475 and hight/2-195<clickedy<hight/2-120:
        status=3
    if width/2-400<clickedx<width/2-325 and hight/2-195<clickedy<hight/2-120:
        status=5

def showhighscore():
    global status
    pygame.draw.rect(screen, GREEN, [width/2-175, hight/2+175, 380, 100])
    screen.blit(defaultfont.render("Back to lobby", True, BLACK), [width/2-150, hight/2+200])
    file = open("names.txt")
    for line in file:
        namelist=line.split(",")
    file.close()
    for i in range(1,6):
        names = defaultfont.render(str(i)+". " + namelist[-i]+":", True, BLACK)
        screen.blit(names, [width/2-175,hight/2-200+(50*i)])
    file = open("highscore.txt")
    for line in file:
        highscorelist=line.split(",")
    file.close()
    for i in range(1,6):
        highscores = defaultfont.render(highscorelist[-i], True, BLACK)
        screen.blit(highscores, [width/2+175,hight/2-200+(50*i)])
    if width/2-175<clickedx<width/2+205 and hight/2+175<clickedy<hight/2+275:
        status=4

def endscreen():
    global status, newhighscore,enter
    screen.blit(defaultfont.render("or press ESCAPE to exit.", True, BLACK), [width/2-325, hight/2+300])
    screen.blit(defaultfont.render("Your score was: " + str(score_player), True,BLACK), [width/2-250, hight/2-200])
    pygame.draw.rect(screen, GREEN, [width/2-200, hight/2+75, 380, 100])
    screen.blit(defaultfont.render("Back to lobby", True, BLACK), [width/2-180, hight/2+100])
    if width/2-200<clickedx<width/2+185 and hight/2+75<clickedy<hight/2+175:
        status=4
        newhighscore=0
        enter=0

def infoscreen():
    global status
    screen.blit(defaultfont.render("This game is about controlling a bird ", True, BLACK), [width/2-425, hight/2-275])
    screen.blit(defaultfont.render("and trying to fly between the green pipes", True, BLACK), [width/2-470, hight/2-225])
    screen.blit(defaultfont.render("without touching them.", True, BLACK), [width/2-270, hight/2-175])
    screen.blit(defaultfont.render("If you want to jump just press SPACE.", True, BLACK), [width/2-425, hight/2-125])
    screen.blit(defaultfont.render("You can also click on the +5 buttons ", True, BLACK), [width/2-415, hight/2-75])
    screen.blit(defaultfont.render("to earn 5 additional points. But be careful, ", True, BLACK), [width/2-490, hight/2-25])
    screen.blit(defaultfont.render("as the more points you collect,", True, BLACK), [width/2-380, hight/2+25])
    screen.blit(defaultfont.render("the harder the game gets.", True, BLACK), [width/2-300, hight/2+75])
    pygame.draw.rect(screen, GREEN, [width/2-175, hight/2+175, 380, 100])
    screen.blit(defaultfont.render("Back to lobby", True, BLACK), [width/2-150, hight/2+200])
    if width/2-175<clickedx<width/2+205 and hight/2+175<clickedy<hight/2+275:
        status=4

def settingsscreen():
    global fps,soundoff,clickedx1,soundeffoff,status,skin
    screen.blit(defaultfont.render("Settings", True, BLACK),[width/2-100, hight/2-300])
    screen.blit(defaultfont.render("FPS:", True, BLACK), [width/2-300, hight/2-200])
    pygame.draw.rect(screen, GREEN, [width/2-150, hight/2-200, 100, 50])
    pygame.draw.rect(screen, GREEN, [width/2, hight/2-200, 100, 50])
    pygame.draw.rect(screen, GREEN, [width/2+150, hight/2-200, 100, 50])
    screen.blit(defaultfont.render("60", True, RED), [width/2-130, hight/2-200])
    screen.blit(defaultfont.render("144", True, RED), [width/2+5, hight/2-200])
    screen.blit(defaultfont.render("240", True, RED), [width/2+155, hight/2-200])
    screen.blit(defaultfont.render("Backgroundmusik:", True, BLACK), [width/2-300, hight/2-100])
    screen.blit(sound, (width/2+200,hight/2-100))
    screen.blit(defaultfont.render("Soundeffects:", True, BLACK), [width/2-300, hight/2])
    screen.blit(sound, (width/2+200,hight/2))
    screen.blit(defaultfont.render("Skin:", True, BLACK),[width/2-300, hight/2+100])
    pygame.draw.rect(screen, GREEN, [width/2-107, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2-7, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2+93, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2+193, hight/2+93, 65, 50])
    pygame.draw.rect(screen, GREEN, [width/2-175, hight/2+175, 380, 100])
    screen.blit(defaultfont.render("Back to lobby", True, BLACK), [width/2-150, hight/2+200])
    if width/2-150<clickedx<width/2-50 and hight/2-200<clickedy<hight/2-150 or fps<90:
        fps=60
        pygame.draw.rect(screen, RED, [width/2-150, hight/2-200, 100, 50])
        screen.blit(defaultfont.render("60", True, GREEN), [width/2-130, hight/2-200])
    if width/2<clickedx<width/2+100 and hight/2-200<clickedy<hight/2-150 or 90<fps<180:
        fps=144
        pygame.draw.rect(screen, RED, [width/2, hight/2-200, 100, 50])
        screen.blit(defaultfont.render("144", True, GREEN), [width/2+5, hight/2-200])
    if width/2+150<clickedx<width/2+250 and hight/2-200<clickedy<hight/2-150 or fps>180:
        fps=240
        pygame.draw.rect(screen, RED, [width/2+150, hight/2-200, 100, 50])
        screen.blit(defaultfont.render("240", True, GREEN), [width/2+155, hight/2-200])
    if width/2+200<clickedx<width/2+250 and hight/2-100<clickedy<hight/2-50:
        if soundoff==0:
            soundoff=1
            pygame.mixer.music.pause()
        else:
            soundoff=0
            pygame.mixer.music.unpause()
    if soundoff==1:
        pygame.draw.line(screen,RED,(width/2+200,hight/2-50),(width/2+250,hight/2-100),5)
    if width/2+200<clickedx<width/2+250 and hight/2<clickedy<hight/2+50:
        if soundeffoff==0:
            soundeffoff=1 
        else:
            soundeffoff=0
    if soundeffoff==1:
        pygame.draw.line(screen,RED,(width/2+200,hight/2+50),(width/2+250,hight/2),5)
    if width/2-107<clickedx<width/2-42 and hight/2+93<clickedy<hight/2+143 or skin==0:
        skin=0
        pygame.draw.rect(screen, RED, [width/2-107, hight/2+93, 65, 50])
    if width/2-7<clickedx<width/2+58 and hight/2+93<clickedy<hight/2+143 or skin==1:
        skin=1
        pygame.draw.rect(screen, RED, [width/2-7, hight/2+93, 65, 50])
    if width/2+93<clickedx<width/2+158 and hight/2+93<clickedy<hight/2+143 or skin==2:
        skin=2
        pygame.draw.rect(screen, RED, [width/2+93, hight/2+93, 65, 50])
    if width/2+193<clickedx<width/2+258 and hight/2+93<clickedy<hight/2+143 or skin==3:
        skin=3
        pygame.draw.rect(screen, RED, [width/2+193, hight/2+93, 65, 50])
    screen.blit(bird_image,( width/2-100,hight/2+100))
    screen.blit(bird_image1,( width/2,hight/2+100))
    screen.blit(bird_image2,( width/2+100,hight/2+100))
    screen.blit(bird_image3,( width/2+200,hight/2+100))
    if width/2-175<clickedx<width/2+205 and hight/2+175<clickedy<hight/2+275:
        status=4

def birdmovement():
    global birdy, jumpduration
    if jumpduration<(20*fpsmultiplier):
        birdy-=(5.25/fpsmultiplier)/ymultiplier
        jumpduration+=1
    else:
        birdy+=(4.5/fpsmultiplier)/ymultiplier
    if birdy<=0:
        birdy=0.1
    elif birdy>=hight-36:
        birdy=(hight-36.1)

def pipemovement():
    global pipex1,pipex2,pipe1reset,pipe2reset,pipey1,pipey2,pipeupdown
    if score_player<=99:
        pipex1-=(6.25/fpsmultiplier)/xmultiplier
        pipex2-=(6.25/fpsmultiplier)/xmultiplier
    elif score_player>99:
        pipex1-=(7.5/fpsmultiplier)/xmultiplier
        pipex2-=(7.5/fpsmultiplier)/xmultiplier
    if pipex1<-50:
        pipex1=width
        pipe1reset=0
    if pipex2<-50:
        pipex2=width
        pipe2reset=0
    if pipe1reset==0:
        pipey1=random.randrange(50,hight-200-50)
        pipe1reset=1
    if pipe2reset==0:
        pipey2=random.randrange(50,hight-200-50)
        pipe2reset=1
    if score_player>=199:
        if pipeupdown<=120*fpsmultiplier:
            pipey1+=0.025*fpsmultiplier
            pipey2-=0.025*fpsmultiplier
            pipeupdown+=1
        elif 120*fpsmultiplier<pipeupdown<=240*fpsmultiplier:
            pipey1-=0.025*fpsmultiplier
            pipey2+=0.025*fpsmultiplier
            pipeupdown+=1
        elif pipeupdown>240*fpsmultiplier:
            pipeupdown=0

def plusfive():
    global yfive,xfive,gotfive,notfive,clickedx,clickedy,yfive,score_player,fiveupdown
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
        if fiveupdown<=60*fpsmultiplier:
            yfive+=0.05*fpsmultiplier
            fiveupdown+=1
        elif 60*fpsmultiplier<fiveupdown<=120*fpsmultiplier:
            yfive-=0.05*fpsmultiplier
            fiveupdown+=1
        elif fiveupdown>120*fpsmultiplier:
            fiveupdown=0

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
        screen.blit(defaultfont.render("Just type your name:", True, BLACK), [width/2-425, hight/2-100])
        img = defaultfont.render(text, True, RED)
        rect = img.get_rect()
        rect.topleft = (width/2+100,hight/2-100)
        cursor = pygame.Rect(rect.topright, (3, rect.height))
        screen.blit(img, (width/2+100,hight/2-100))       
        rect.size=img.get_size()
        cursor.topleft = rect.topright
        if time.time() % 1 > 0.5 and enter ==0:
            pygame.draw.rect(screen, RED, cursor)
            screen.blit(defaultfont.render(("Press ENTER to save your name."), True,BLACK), [width/2-425, hight/2])
    screen.blit(defaultfont.render("The Highscore is: " + highscore_list[-1], True, BLACK), [width/2-280, hight/2-150])
    
def movingbackground():
    global background1x,background2x,fpsmultiplier
    background1x-=0.8/fpsmultiplier
    background2x-=0.8/fpsmultiplier
    if background1x<=-width:
        background1x=width
    if background2x<=-width:
        background2x=width
    screen.blit(customizedsky,(background1x,0))
    screen.blit(customizedsky,(background2x,0))

# main programm loop
while not done:
    fpsmultiplier=fps/60
    
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
            elif event.key == pygame.K_h and (status==4):
                status=2
            elif event.key == pygame.K_RETURN and status==4:
                status = 0
                birdy=hight/2 
                score_player=0
                pipex1=width
                pipex2=width+(width/2)
            elif event.key == pygame.K_SPACE and status==0 and clickedspace==0:
                jumpduration = 0
                clickedspace=1
                if soundeffoff==0:
                    jump.play()
            elif newhighscore>0:
                if event.key == pygame.K_BACKSPACE and enter!=1:
                    if len(text)>0:
                        text = text[:-1]
                elif event.key == pygame.K_RETURN and enter!=1:
                    file = open("names.txt",'a')
                    file.write(",")
                    file.write(text)
                    file.close()
                    enter=1
                else:
                    if enter!=1:
                        text += event.unicode
                img = defaultfont.render(text, True, RED)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and status==0:
                clickedspace=0
                
# background
    movingbackground()
    
# running game
    if status==0:
        plusfive()
        pipemovement()
        birdmovement()
        collisioncheck()
        screen.blit(defaultfont.render("Score: " + str(score_player), True, BLACK),(20,20))
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

# pre game lobby
    elif status==4:
        prescreen()

# infoscreen
    elif status==5:
        infoscreen()

# update screen
    
    clock.tick(fps)
    screen.blit(fpssize.render(str(int(clock.get_fps())), 1, RED), (width-50,10))
    pygame.display.flip()
    clickedx=0
    clickedy=0

# bye
pygame.quit()