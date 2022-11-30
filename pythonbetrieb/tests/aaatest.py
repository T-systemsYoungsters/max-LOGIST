import pygame
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
def modifyGrid(grid, row, column):
    if (row ) > 0:
        grid[row - 1][column] = 1
    if (row)<9:
        grid[row + 1][column] = 1
    if (column)>0:
        grid[row][column-1] = 1
    if (column)<9:
        grid[row][column+1] = 1
pygame.init()
screen = pygame.display.set_mode([255, 255])
pygame.display.set_caption("Grid Clicker Application")
done = False 
clock = pygame.time.Clock() 
width = 20
margin = 5
grid = []
for row in range(0, 10):
    grid.append([])
    for column in range(0, 10):
        grid[row].append(0)
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] // (width + margin)
            modifyGrid(grid, row, column)
            grid[row][column] = 1
    screen.fill(BLACK)
    color = WHITE
    for column in range(0, 10):
        for row in range(0, 10):
            if (grid[row][column] == 1):
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(screen, color,[margin + column * (width + margin),margin + row * (width + margin),width,width])  
    pygame.display.flip()
    clock.tick(60)
pygame.quit()