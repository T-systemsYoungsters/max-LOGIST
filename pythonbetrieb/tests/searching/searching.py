# file = open((r"C:\Users\A200162668\Desktop\Python\pythonbetrieb\tests\searching\villains.txt"))
# for line in file:
#     line = line.strip() # -> Leerzeichen entfernen
#     print(line)
# file.close() # -> nicht unnötig offen lassen
# name_list = [] # -> um alle Namen in eine Liste einzutragen
# for line in file:
#     line = line.strip()
#     name_list.append(line)
# file.close()
# key = "Morgiana the Shrew"
# i = 0
# while i < len(name_list) and name_list[i] != key: # -> um nach Namen in der Liste, linear zu suchen
#     i += 1
# if i < len(name_list):
#     print( "The name is at position", i)
# else:
#     print( "The name was not in the list." )
# --- Binary search
# name_list = []
# for line in file:
#     line = line.strip()
#     name_list.append(line)
# file.close()
# key = "Morgiana the Shrew"
# lower_bound = 0
# upper_bound = len(name_list)-1
# found = False
# # Loop, bis man den Gegenstand findet oder man die oberen/unteren Grenzen sich treffen
# while lower_bound <= upper_bound and not found:
#     middle_pos = (lower_bound + upper_bound) // 2
#     # man findet heraus, ob man die untere Grenze nach oben oder die obere Grenze nach unten bewegen, oder ob man es gefunden habt
#     if name_list[middle_pos] < key:
#         lower_bound = middle_pos + 1
#     elif name_list[middle_pos] > key:
#         upper_bound = middle_pos - 1
#     else:
#         found = True
# if found:
#     print( "The name is at position", middle_pos)
# else:
#     print( "The name was not in the list." )
# 
# def binary_search(list, key):
#     lower_bound = 0
#     upper_bound = len(list)-1
#     found = False
#     while lower_bound <= upper_bound and not found:
#         r = (lower_bound + upper_bound) // 2
#         if list[r] < key:
#             lower_bound = r + 1
#         elif list[r] > key:
#             upper_bound = r - 1
#         else:
#             found = True
#     if found:
#         return r
#     else:
#         return -1
# my_list = [0, 3, 5, 12, 18, 50, 70, 78]
# r = binary_search(my_list, 3)
# if r == 1:
#     print("Test A passed")
# else:
#     print("Test A failed. Expected 1 and got", r)
# r = binary_search(my_list, 5)
# if r == 2:
#     print("Test B passed")
# else:
#     print("Test B failed. Expected 2 and got", r)
# r = binary_search(my_list, 10)
# if r == -1:
#     print("Test C passed")
# else:
#     print("Test C failed. Expected -1 and got", r)
    
# def linear_search(list, key):
#     i = 0
#     while i < len(list) and list[i] != key:
#         i += 1
#     if i < len(list):
#         return i
#     else:
#         return -1
# my_list = [4, 3, 2, 1, 5, 7, 6]
# r = linear_search(my_list, 3)
# if r == 1:
#     print("Test A passed")
# else:
#     print("Test A failed. Expected 1 and got", r)
# r = linear_search(my_list, 2)
# if r == 2:
#     print("Test B passed")
# else:
#     print("Test B failed. Expected 2 and got", r)
# r = linear_search(my_list, 10)
# if r == -1:
#     print("Test C passed")
# else:
#     print("Test C failed. Expected -1 and got", r)

# def detect_positive(list):
#     i = 0
#     while i < len(list) and list[i] < 0:
#         i += 1
#     if i < len(list):
#         return True
#     else:
#         return False
# test_list=[-2,-5,-3,3]
# if detect_positive(test_list):
#     print("This list contains at least 1 positiv number.")
# else:
#     print("This list does not contain a positiv number.")