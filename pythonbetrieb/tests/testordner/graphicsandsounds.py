import pygame
pygame.init()
screen = pygame.display.set_mode([1130, 647])
pygame.display.set_caption("My Game")
time=pygame.time.Clock()
done = False
# wichtig zu wissen: jpg kacke weil das die Farben teilweise abändert. lieber png oder gif verwenden -> opengameart.org
background_image = pygame.image.load((r"C:\Users\A200162668\Desktop\Python\pythonlernen\pythonbetrieb\tests\testordner\background.jpg")).convert()
t_image = pygame.image.load((r"C:\Users\A200162668\Desktop\Python\pythonlernen\pythonbetrieb\tests\testordner\t.png")).convert()
# filtert die angegebene Farbe heraus
t_image.set_colorkey((0,0,0))
pygame.mouse.set_visible(0)
# auch bei opengameart.org
click_sound = pygame.mixer.Sound((r"C:\Users\A200162668\Desktop\Python\pythonlernen\pythonbetrieb\tests\testordner\laser5.ogg"))
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    screen.blit(background_image, [0, 0])
    mouse=pygame.mouse.get_pos()
    xpos=mouse[0]
    ypos=mouse[1]
    screen.blit(t_image, [xpos, ypos])
    pygame.display.flip()
time.tick(20)
pygame.quit()