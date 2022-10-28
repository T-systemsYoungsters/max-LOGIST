# 1.
# number = 1
# stop = 2
# rows = 9
# for i in range(rows):
#     for column in range(1, stop):
#         print(number+9, end=' ')
#         number += 1
#     print("")
#     stop += 1

# 2.
# n=int(input("Bitte geben sie hier die Größe des Kästchens an: "))
# for a in range(0,n):
#     print("O",end='')
# print()
# for a in range(0,n-2):
#     print("O",end='')
#     for a in range(0,n-2):
#         print(" ",end='')
#     print("O")
# for a in range(0,n):
#     print("O",end='')

# 3.
n=int(input("Bitte geben sie hier ihren gewünschten Wert an: "))
for i in range(0, n + 1, 1):
    for j in range(i + 1, n + 1, 1):
        print(j*2-1, end=' ')
    print()
for i in range(n + 1,0,  -1):
    for j in range(i , n + 1, 1):
        print(j*2-1, end=' ')
    print()
for i in range(0, n + 1, 1):
    for j in range(n ,i ,  -1):
        print(j*2-1, end=' ')
    print()
for i in range(n + 1,0,  -1):
    for j in range(i , n + 1, 1):
        print(j*2-1, end=' ')
    print()

# 4.
# import pygame
# pygame.init()
# screen = pygame.display.set_mode([500, 500])
# pygame.display.set_caption("test")
# time=pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((255, 255, 255))
#     for offset in range(0, 500, 14):
#        pygame.draw.rect(screen, (226, 0, 116), [0+offset, 0, 10, 10])
#        x=offset
#        for offset in range(0, 500, 14):
#            pygame.draw.rect(screen, (226, 0, 116), [x, 0+offset, 10, 10])
#     pygame.display.flip()
# time.tick(20)
# pygame.quit()