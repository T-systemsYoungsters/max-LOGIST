# # Import und Initialisierung von pygame
# import pygame
# pygame.init()
# # fenster erstellen
# screen = pygame.display.set_mode([600, 500])
# # Fenstertitel setzen
# pygame.display.set_caption("Telekom an die 1")
# # steuert wie oft das Fenster geupdated wird
# zeit=pygame.time.Clock()
# # laufen lassen bis Fenster geschlossen wird
# running = True
# while running:
# # Test ob Fenster geschlossen wurde
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# # Hintergrund mit Farbe füllen
#     screen.fill((255, 255, 255))
# # Zeichnen von Rechtecken -> das was später gezeichnet wird überdeckt das von davor
#     pygame.draw.rect(screen, (226, 0, 116), [50, 50, 300, 100])
#     pygame.draw.rect(screen, (226, 0, 116), [150, 150, 100, 300])
#     pygame.draw.rect(screen, (226, 0, 116), [50, 250, 50, 50])
#     pygame.draw.rect(screen, (226, 0, 116), [300, 250, 50, 50])
#     pygame.draw.rect(screen, (226, 0, 116), [400, 250, 50, 50])
#     pygame.draw.rect(screen, (226, 0, 116), [500, 250, 50, 50])
# # schreiben im Fenster
#     schrift = pygame.font.SysFont('Arial', 25, True, False)
#     text = schrift.render("Erleben, was verbindet.", True, (226, 0, 116))
#     screen.blit(text, [300, 350])
# # updated das Fenster mit dem was man gezeichnet hat
#     pygame.display.flip()
# # auf 20 fps beschränkt
# zeit.tick(20)
# # schließen von pygame
# pygame.quit()
import pygame # Drawing functions

# Constant Color Defines
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def modifyGrid(grid, row, column):
    if (row - 1) > 0:
        grid[row - 1][column] = 1
    if (row+1)<9:
        grid[row + 1][column] = 1
    if (column+1)<9:
        grid[row][column-1] = 1
    if (column+1)<9:
        grid[row][column+1] = 1
# Initialization of Window Properties
pygame.init()
screen = pygame.display.set_mode([255, 255])
pygame.display.set_caption("Grid Clicker Application")
  
# Initialization of Program Variables
playing = True # Runs the game loop until the user closes the window
clock = pygame.time.Clock() # Used to manage frames per second
    
# Visual Grid Variables
width = 20
margin = 5
    
# Logical Grid Variables
grid = []
    
for row in range(0, 10):
    grid.append([])
        
    for column in range(0, 10):
        grid[row].append(0)
    
    # Set an element of the grid to 1 to demonstrate color changes
grid[1][5] = 1
    
    # Main Program Loop
while (playing == True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mPos = pygame.mouse.get_pos()
            column = mPos[0] // (width + margin)
            row = mPos[1] // (width + margin)
            modifyGrid(grid, row, column)
            grid[row][column] = 1
            print("Click Square: [" + str(row) + "," + str(column) + "]")
                
    
        # New frame clear
    screen.fill(BLACK)
        
        # Start of Logic Processing
    color = WHITE
        # End of Logic Processing
    
        # Start of Drawing New Frame
        
        # Loop through the visual grid
    for column in range(0, 10):
        for row in range(0, 10):
                
                # Decide on what color to use for square rendering
            if (grid[row][column] == 1):
                color = GREEN
            else:
                color = WHITE
                
                # Draw the square
            pygame.draw.rect(screen, color,[margin + column * (width + margin),margin + row * (width + margin),width,width])  
        # End of Drawing New Frame
    
        # Display drawn frame
    pygame.display.flip()
    clock.tick(60)
    
        # End of Draw Loop
    
pygame.quit()
    # End of main()

