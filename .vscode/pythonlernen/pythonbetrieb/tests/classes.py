# class Character(): # -> immer groß schreiben
#     name = "Link"
#     sex = "Male"
#     max_hit_points = 50
#     current_hit_points = 50
#     max_speed = 10
#     armor_amount = 8
# def displaycharacter(mycharacter):
#     print(mycharacter.name,mycharacter.sex)
# mydude=Character()
# mydude.name="Max"
# mydude.sex="Male"
# displaycharacter(mydude)
# class Dog():
#     age = 0
#     name = ""
#     weight = 0
#     def bark(self):
#         print(self.name,"says 'Bark'")
# my_dog = Dog()
# my_dog.name = "Spot"
# my_dog.weight = 20
# my_dog.age = 3
# my_dog.bark()
# import pygame
# class Ball():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.change_x = 0
#         self.change_y = 0
#         self.size = 10
#         self.color = [255,255,255]
#     def move(self):
#         self.x += self.change_x
#         self.y += self.change_y
#     def draw(self, screen):
#         pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )
# class Dog():
#     name=""
#     def __init__(self,myname): # -> wird immer aufgerufen wenn ein neuer Hund erschaffen wird
#         self.name = ""
#         print("A new dog is born!")
#         self.name=myname
# my_dog = Dog("Spot")
# print("The dogs name is:",my_dog.name)
# class Boat(): # -> Hauptklasse
#     def __init__(self):
#         self.tonnage = 0
#         self.name = ""
#         self.is_docked = True
#     def dock(self):
#         if self.is_docked:
#             print("You are already docked.")
#         else:
#             self.is_docked = True
#             print("Docking")
#     def undock(self):
#         if not self.is_docked:
#             print("You aren't docked.")
#         else:
#             self.is_docked = False
#             print("Undocking")
# class Submarine(Boat): # -> spezifische Unterklasse, die auf die Hauptklasse zugreift und sie ohne sie extra einzubauen mit verwendet und nur etwas für einen bestimmten Fall hinzufügt
#     def submerge(self):
#         print("Submerge!")
