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
def player(filename):
    image = pygame.image.load(filename)
    rect = image.get_rect()
    change_x = 0
    change_y = 0
def show_score(scoreofplayer):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score: " + str(scoreofplayer), True, (255,255,255))
    screen.blit(score,(20,20))
screen = pygame.display.set_mode([1000, 750])
pygame.display.set_caption("My Game")
time=pygame.time.Clock()
# flappybird=pygame.image.load((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\flappybird.png")).convert()
jump=pygame.mixer.Sound((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\jump.mp3"))
point=pygame.mixer.Sound((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\point.mp3")) 
# flappybird.set_colorkey((255,255,255))
bird = player((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\flappybird.png"))
done = False
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                a = 0
                jump.play()
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
    pipe2=pygame.draw.rect(screen, (0, 200, 0), [pipex1, pipey1+300, 50, 600])
    pipe3=pygame.draw.rect(screen, (0, 200, 0), [pipex2, 0, 50, pipey2])
    pipe4=pygame.draw.rect(screen, (0, 200, 0), [pipex2, pipey2+300, 50, 600])
    bird=pygame.image.load((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\flappybird\flappybird.png"))
    rect = bird.get_rect()
    rect.x =birdy
    rect.y =birdy
    collide1 = rect.colliderect(pipe1)
    collide2 = rect.colliderect(pipe2)
    collide3 = rect.colliderect(pipe3)
    collide4 = rect.colliderect(pipe4)
    if collide1==1 or collide2==1 or collide3==1 or collide4==1:
        done=True
    if 99.7<=pipex1<=100 or 99.7<=pipex2<=100:
        score_player+=1
        point.play()
    show_score(score_player)
    pygame.display.flip()
time.tick(20)
print("Ihr Score war:",score_player)
pygame.quit()