import pygame
pygame.init()
screen = pygame.display.set_mode([600, 600])
pygame.display.set_caption("Telekom an die #1!")
time=pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (226, 0, 116), [50, 50, 300, 100])
    pygame.draw.rect(screen, (226, 0, 116), [150, 150, 100, 300])
    pygame.draw.rect(screen, (226, 0, 116), [50, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [300, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [400, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [500, 250, 50, 50])
    pygame.draw.rect(screen, (226, 0, 116), [20, 20, 560, 560], 5)
    for offset in range(0, 15, 5):
        pygame.draw.line(screen, (226, 0, 116), [32, 500 + offset], [568, 500 + offset], 3)
        pygame.draw.line(screen, (226, 0, 116), [55, 560 + offset], [545, 560 + offset], 3)
    font = pygame.font.SysFont('Arial', 48, True, False)
    text1 = font.render("Erleben, was verbindet.", True, (226, 0, 116))
    text2 = font.render("#DABEI sein ist alles!", True, (226, 0, 116))
    screen.blit(text1, [32, 450])
    screen.blit(text2, [55, 510])
    pygame.display.flip()
    
time.tick(20)
pygame.quit()