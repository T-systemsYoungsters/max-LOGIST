# gleicher Schneeman in jeder Ecke
# import pygame
# def draw_snowman(screen, x, y):
#     pygame.draw.ellipse(screen, WHITE, [35 + x, 0 + y, 25, 25])
#     pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
#     pygame.draw.ellipse(screen, WHITE, [0 + x, 65 + y, 100, 100])
# pygame.init()
# BLACK = [0, 0, 0]
# WHITE = [255, 255, 255]
# size = [400, 500]
# screen = pygame.display.set_mode(size)
# done = False
# clock = pygame.time.Clock()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     screen.fill(BLACK)
#     draw_snowman(screen, 10, 10)
#     draw_snowman(screen, 300, 10)
#     draw_snowman(screen, 10, 300)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
# 
# gleicher Stickman 
# import pygame
# pygame.init()
# BLACK = [0, 0, 0]
# WHITE = [255, 255, 255]
# RED=[255,0,0]
# def stickman(screen,x,y):
#     # Head
#     pygame.draw.ellipse(screen, BLACK, [96+x,83+y,10,10], 0)
#     # Legs
#     pygame.draw.line(screen, BLACK, [100+x,100+y], [105+x,110+y], 2)
#     pygame.draw.line(screen, BLACK, [100+x,100+y], [95+x,110+y], 2)
#     # Body
#     pygame.draw.line(screen, RED, [100+x,100+y], [100+x,90+y], 2)
#     # Arms
#     pygame.draw.line(screen, RED, [100+x,90+y], [104+x,100+y], 2)
#     pygame.draw.line(screen, RED, [100+x,90+y], [96+x,100+y], 2)
# size = [400, 500]
# screen = pygame.display.set_mode(size)
# done = False
# clock = pygame.time.Clock()
# while done==False:
#     clock.tick(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     screen.fill(WHITE)
#     stickman(screen,200,200)
#     stickman(screen,0,0)
#     stickman(screen,200,0)
#     stickman(screen,0,200)
#     pygame.display.flip()
# pygame.quit()
# 
# Mit Mauseingabe arbeiten
# import pygame
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# def draw_stick_figure(screen, x, y):
#     # Head
#     pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
#     # Legs
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
#     # Body
#     pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
#     # Arms
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
# pygame.init()
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("My Game")
# done = False
# clock = pygame.time.Clock()
# # Mauszeiger unsichtbar machen
# pygame.mouse.set_visible(0)
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     pos = pygame.mouse.get_pos()
#     x = pos[0]
#     y = pos[1]
#     screen.fill(WHITE)
#     draw_stick_figure(screen, x, y)
#     pygame.display.flip()
#     clock.tick(60)
# pygame.quit()
# 
# Mit Tastatureingabe arbeiten
# import pygame
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# def draw_stick_figure(screen, x, y):
#     # Head
#     pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
#     # Legs
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
#     # Body
#     pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
#     # Arms
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
# pygame.init()
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("My Game")
# done = False
# clock = pygame.time.Clock()
# x_speed = 0
# y_speed = 0
# x_coord = 10
# y_coord = 10
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         # prüfen auf Eingabe des Users
#         elif event.type == pygame.KEYDOWN:
#             # prüfen ob es eine Pfeiltaste war unnd wenn ja dann Bewegung umsetzen
#             if event.key == pygame.K_LEFT:
#                 x_speed = -3
#             elif event.key == pygame.K_RIGHT:
#                 x_speed = 3
#             elif event.key == pygame.K_UP:
#                 y_speed = -3
#             elif event.key == pygame.K_DOWN:
#                 y_speed = 3
#         # prüfen ob die Taste wieder losgelassen wurde
#         elif event.type == pygame.KEYUP:
#             # wenn die losgelassene Taste eine Pfeiltaste war wird die Bewegung wieder auf 0 gesetzt
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 x_speed = 0
#             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                 y_speed = 0
#     # Zeichnung mit Geschwindigkeitsvektor bewegen
#     x_coord = x_coord + x_speed
#     y_coord = y_coord + y_speed
#     screen.fill(WHITE)
#     draw_stick_figure(screen, x_coord, y_coord)
#     pygame.display.flip()
#     clock.tick(60) 
# pygame.quit()
# 
# Tastenbezeichnungen
# Pygame Code	ASCII	Common Name
# K_BACKSPACE	\b	backspace
# K_RETURN	\r	return
# K_TAB	\t	tab
# K_ESCAPE	^[	escape
# K_SPACE	 	space
# K_COMMA	,	comma sign
# K_MINUS	-	minus
# K_PERIOD	.	period slash
# K_SLASH	/	forward
# K_0	0	0
# K_1	1	1
# K_2	2	2
# K_3	3	3
# K_4	4	4
# K_5	5	5
# K_6	6	6
# K_7	7	7
# K_8	8	8
# K_9	9	9
# K_SEMICOLON	;	semicolon sign
# K_EQUALS	=	equals sign
# K_LEFTBRACKET	[	left
# K_RIGHTBRACKET	]	right
# K_BACKSLASH	\	backslash bracket
# K_BACKQUOTE	`	grave
# K_a	a	a
# K_b	b	b
# K_c	c	c
# K_d	d	d
# K_e	e	e
# K_f	f	f
# K_g	g	g
# K_h	h	h
# K_i	i	i
# K_j	j	j
# K_k	k	k
# K_l	l	l
# K_m	m	m
# K_n	n	n
# K_o	o	o
# K_p	p	p
# K_q	q	q
# K_r	r	r
# K_s	s	s
# K_t	t	t
# K_u	u	u
# K_v	v	v
# K_w	w	w
# K_x	x	x
# K_y	y	y
# K_z	z	z
# K_DELETE	delete	
# K_KP0	keypad	0
# K_KP1	keypad	1
# K_KP2	keypad	2
# K_KP3	keypad	3
# K_KP4	keypad	4
# K_KP5	keypad	5
# K_KP6	keypad	6
# K_KP7	keypad	7
# K_KP8	keypad	8
# K_KP9	keypad	9 period
# K_KP_PERIOD	.	keypad divide
# K_KP_DIVIDE	/	keypad multiply
# K_KP_MULTIPLY	*	keypad minus
# K_KP_MINUS	-	keypad plus
# K_KP_PLUS	+	keypad enter
# K_KP_ENTER	\r	keypad equals
# K_KP_EQUALS	=	keypad
# K_UP	up	arrow
# K_DOWN	down	arrow
# K_RIGHT	right	arrow
# K_LEFT	left	arrow
# K_INSERT	insert	
# K_HOME	home	
# K_END	end	
# K_PAGEUP	page	up
# K_PAGEDOWN	page	down
# K_F1	F1	
# K_F2	F2	
# K_F3	F3	
# K_F4	F4	
# K_F5	F5	
# K_F6	F6	
# K_F7	F7	
# K_F8	F8	
# K_F9	F9	
# K_F10	F10	
# K_F11	F11	
# K_F12	F12	
# K_NUMLOCK	numlock	
# K_CAPSLOCK	capslock	
# K_RSHIFT	right	shift
# K_LSHIFT	left	shift
# K_RCTRL	right	ctrl
# K_LCTRL	left	ctrl
# K_RALT	right	alt
# K_LALT	left	alt 
# 
# mit Controllereingabe arbeiten
# import pygame
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# def draw_stick_figure(screen, x, y):
#     # Head
#     pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
#     # Legs
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
#     pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
#     # Body
#     pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
#     # Arms
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
#     pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
# pygame.init()
# size = [700, 500]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("My Game")
# done = False
# clock = pygame.time.Clock()
# x_coord = 10
# y_coord = 10
# # prüfen ob ein controller angeschlossen ist
# joystick_count = pygame.joystick.get_count()
# if joystick_count == 0:
#     print("Error, I didn't find any joysticks.")
# else:
#     # controller initialisieren
#     my_joystick = pygame.joystick.Joystick(0)
#     my_joystick.init()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     # Bei vorhandenem Controller:
#     if joystick_count != 0:
#         # prüfen wo der Controller sich befindet
#         # Ausgabe ist zwischen -1.0 und +1.0
#         horiz_axis_pos = my_joystick.get_axis(0)
#         vert_axis_pos = my_joystick.get_axis(1)
#         x_coord = x_coord + int(horiz_axis_pos * 10)
#         y_coord = y_coord + int(vert_axis_pos * 10)
#     screen.fill(WHITE)
#     draw_stick_figure(screen, x_coord, y_coord)
#     pygame.display.flip()
#     clock.tick(60)
#     pygame.quit()