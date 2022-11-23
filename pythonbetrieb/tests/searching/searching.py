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