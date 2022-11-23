import random
import pygame
pygame.init()
pipex1=1000
pipex2=1500
birdy=350 
a=1000
b=0
c=0
score_player=0
status=-1
def show_score(scoreofplayer):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score: " + str(scoreofplayer), True, (255,255,255))
    screen.blit(score,(20,20))
screen = pygame.display.set_mode([1000, 750])
pygame.display.set_caption("My Game")
time=pygame.time.Clock()
jump=pygame.mixer.Sound((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\jump.mp3"))
point=pygame.mixer.Sound((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\point.mp3")) 
bird_image=pygame.image.load((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\flappybird.png"))
bird_image.set_colorkey((255,255,255))
bird = bird_image.get_rect()
done = False
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RETURN:
                status = 0
                birdy=350
                score_player=0
                pipex1=1000
                pipex2=1500
            elif event.key == pygame.K_KP_ENTER:
                status = 0
                birdy=350
                score_player=0
                pipex1=1000
                pipex2=1500
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                a = 0
                jump.play()
    if status==-1:
        screen.fill((0, 0, 200))
        schrift = pygame.font.SysFont('freesansbold.ttf', 50, True, False)
        text = schrift.render("Press ENTER to start.", True, (255,255,255))
        screen.blit(text, [250, 350])
    elif status==0:
        pipex1-=0.3
        pipex2-=0.3
        birdy+=0.3
        if pipex1<-50:
            pipex1=1000
            b=0
        if pipex2<-50:
            pipex2=1000
            c=0
        if b==0:
            pipey1=random.randrange(50,400)
            b=1
        if c==0:
            pipey2=random.randrange(50,400)
            c=1
        if a<150:
            birdy-=1
            a+=1
        if birdy<=0:
            birdy=0.1
        elif birdy>=700:
            birdy=699.9
        screen.fill((0, 0, 200))
        pipe1=pygame.draw.rect(screen, (0, 200, 0), [pipex1, 0, 50, pipey1])
        pipe2=pygame.draw.rect(screen, (0, 200, 0), [pipex1, pipey1+170, 50, 600])
        pipe3=pygame.draw.rect(screen, (0, 200, 0), [pipex2, 0, 50, pipey2])
        pipe4=pygame.draw.rect(screen, (0, 200, 0), [pipex2, pipey2+170, 50, 600])
        bird.x =100
        bird.y =birdy
        collide1 = bird.colliderect(pipe1)
        collide2 = bird.colliderect(pipe2)
        collide3 = bird.colliderect(pipe3)
        collide4 = bird.colliderect(pipe4)
        if collide1==1 or collide2==1 or collide3==1 or collide4==1:
            status=1
        else:
            if 99.7<=pipex1<=100 or 99.7<=pipex2<=100:
                score_player+=1
                point.play()
        show_score(score_player) 
        screen.blit(bird_image,( 100,birdy))
    elif status==1:
        screen.fill((0, 0, 200))
        font = pygame.font.SysFont('freesansbold.ttf', 50, True, False)
        text = font.render("Press ENTER to restart", True, (255,255,255))
        text1 = font.render("or press ESCAPE to exit.", True, (255,255,255))
        text2 = font.render("Your score was: " + str(score_player), True, (255,255,255))
        highscore_list= ["0"]
        file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\highscore.txt"))
        for line in file:
            line = line.strip()
            highscore_list.append(line)
        g = str(score_player)
        file.close()
        if g > highscore_list[-1]:
            file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\highscore.txt"),'w')
            file.write(g)
        file.close()
        text3 = font.render("The previous Highscore is: " + highscore_list[-1], True, (255,255,255))
        screen.blit(text, [250, 330])
        screen.blit(text1, [245, 370])
        screen.blit(text2, [250, 410])
        screen.blit(text3, [250, 450])
    pygame.display.flip()
time.tick(20)
pygame.quit()