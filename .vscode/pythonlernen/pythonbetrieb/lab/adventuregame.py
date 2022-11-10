done=False
room_list=[]
room=["You are in the veranda. There is a passage to the east and south.", None, 1, 2 ,None]
room_list.append(room)
room=["You are in the bath. There is a passage to the west.", None, None, None, 0]
room_list.append(room)
room=["You are in the livingroom. There is a passage to the north, east, south and west.", 0, 3, 5, 4]
room_list.append(room)
room=["You are in the bedroom. There is a passage to the west.", None,None,None, 2]
room_list.append(room)
room=["You are on the balcony. There is a passage to the east.",None,2,None,None]
room_list.append(room)
room=["You are in the diningroom. There is a passage to the north and east.", 2, 6,None,None]
room_list.append(room)
room=["You are in the kitchen. There is a passage to the west.",None,None,None,5]
room_list.append(room)
current_room=0
while done == False:
    print()
    print(room_list[current_room][0])
    choice=input("Do you want to go to the north(n), the east(e), the south(s) or the west(w)? (Q=Quit)")
    if choice=="n" :
        next_room=room_list[current_room][1]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif choice=="e" :
        next_room=room_list[current_room][2]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif choice=="s" :
        next_room=room_list[current_room][3]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif choice=="w" :
        next_room=room_list[current_room][4]
        if next_room==None:
            print("You can't go that way.")
        else:
            current_room=next_room
    elif choice=="Q" or choice=="q":
        done=True
    else:
        print("Wrong input.")