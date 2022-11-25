# def f():
#     g()
#     print("f")
# def g():
#     print("g")
# f()

# def f():
#     print("Hello")
#     f()
# f()

# def f(level):
#     print("Recursion call, level",level)
#     if level < 10:
#         f(level+1)
# f(1)

# # This program calculates a factorial WITHOUT using recursion
# def factorial_nonrecursive(n):
#     answer = 1
#     for i in range(2, n + 1):
#         print(i, "*", answer, "=", i * answer)
#         answer = answer * i
#     return answer
# print("I can calculate a factorial!")
# user_input = input("Enter a number:")
# n = int(user_input)
# answer = factorial_nonrecursive(n)
# print(answer)
# # This program calculates a factorial WITH recursion
# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         x = factorial_recursive(n - 1)
#         print( n, "*", x, "=", n * x )
#         return n * x
 
# print("I can calculate a factorial!")
# user_input = input("Enter a number:")
# n = int(user_input)
# answer = factorial_recursive(n)
# print(answer)

# Recursive Rectangles
# import pygame
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# def recursive_draw(x, y, width, height):
#     pygame.draw.rect(screen, BLACK,[x, y, width, height],1)
#     if(width > 28):
#         x += width * .1
#         y += height * .1
#         width *= .8
#         height *= .8
#         recursive_draw(x, y, width, height)
# pygame.init()
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("My Game")
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     screen.fill(WHITE)
#     recursive_draw(0, 0, 700, 500)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()

# Recursive Fractal
# import pygame
# black = (0, 0, 0)
# white = (255, 255, 255) 
# def recursive_draw(x, y, width, height, count):
#     pygame.draw.line(screen,
#                      black,
#                      [x + width*.25, height // 2 + y],
#                      [x + width*.75, height // 2 + y],
#                      3)
#     pygame.draw.line(screen,
#                      black,
#                      [x + width * .25, (height * .5) // 2 + y],
#                      [x + width * .25,  (height * 1.5) // 2 + y],
#                      3)
#     pygame.draw.line(screen,
#                      black,
#                      [x + width * .75, (height * .5) // 2 + y],
#                      [x + width * .75, (height * 1.5) // 2 + y],
#                      3)
#     if count > 0:
#         count -= 1
#         recursive_draw(x, y, width // 2, height // 2, count)
#         recursive_draw(x + width // 2, y, width // 2, height // 2, count)
#         recursive_draw(x, y + width // 2, width // 2, height // 2, count)
#         recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)
# pygame.init()
# size = [700, 700]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("My Game")
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     screen.fill(white)
#     fractal_level = 3
#     recursive_draw(0, 0, 700, 700, fractal_level)
#     pygame.display.flip()
#     clock.tick(20)
# pygame.quit()

# Non-recursive binary search
# def binary_search_nonrecursive(search_list, key):
#     lower_bound = 0
#     upper_bound = len(search_list) - 1
#     found = False
#     while lower_bound < upper_bound and found == False:
#         middle_pos = (lower_bound + upper_bound) // 2
#         if search_list[middle_pos] < key:
#             lower_bound = middle_pos + 1
#         elif search_list[middle_pos] > key:
#             upper_bound = middle_pos
#         else:
#             found = True
#     if found:
#         print( "The name is at position",middle_pos)
#     else:
#         print( "The name was not in the list." )
# binary_search_nonrecursive(name_list,"Morgiana the Shrew")
# Recursive binary search
# def binary_search_recursive(search_list, key, lower_bound, upper_bound):
#     middle_pos = (lower_bound + upper_bound) // 2
#     if search_list[middle_pos] < key:
#         binary_search_recursive(search_list,
#                                 key,
#                                 middle_pos + 1,
#                                 upper_bound)
#     elif search_list[middle_pos] > key:
#         binary_search_recursive(search_list,
#                                 key,
#                                 lower_bound,
#                                 middle_pos )
#     else:
#         print("Found at position", middle_pos)
# lower_bound = 0
# upper_bound = len(name_list) - 1
# binary_search_recursive(name_list,"Morgiana the Shrew",lower_bound,upper_bound)
