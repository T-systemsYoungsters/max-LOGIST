import random
miles=0
thirst=0
tired=0
natives=-20
drinks=5
dead=0
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")
done=False
while done==False:
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print()
    choice=input("What do you want to do? ")
    if choice=="q" or choice=="Q":
        done=True
    elif choice=="e" or choice=="E":
        print()
        print("You traveled",miles,"miles.")
        print("The natives are",miles-natives,"miles behind you.")
        print("You have",drinks,"drinks left in your canteen.")
        print()
    elif choice=="d" or choice=="D":
        tired=0
        natives=natives+random.randrange(7,15)
        print("Your camel is happy but the natives are coming closer.")
    elif choice=="c" or choice=="C":
        miles=miles+random.randrange(10,21)
        print("You traveled",miles,"miles.")
        thirst=thirst+1
        tired=tired+random.randrange(1,3)
        natives=natives+random.randrange(7,15)
    elif choice=="b" or choice=="B":
        miles=miles+random.randrange(5,13)
        print("You traveled",miles,"miles.")
        tired=tired+1
        thirst=thirst+1
        natives=natives+random.randrange(7,15)
    elif choice=="a" or choice=="A":
        if drinks>0:
            drinks=drinks-1
            thirst=0
        else:
            print()
            print("You don`t have any drinks left.")
            print()
    else:
        print()
        print("Wrong letter!")
        print()
    if thirst>4 and thirst<=6 and dead==0:
        print()
        print("You are thirsty!")
        print()
    elif thirst>6:
        print()
        print("You died of thirst!")
        print()
        done=True
        dead=1
    if tired>5 and tired<=8 and dead==0:
        print()
        print("Your camel is getting tired!")
        print()
    elif tired>8:
        print()
        print("Your camel is dead!")
        print()
        done=True
        dead=1
    if natives>=miles:
        print()
        print("You got caught by the natives.")
        print()
        done=True
        dead=1
    elif miles-natives<15 and dead==0:
        print()
        print("The natives are coming closer!")
        print()
    if miles>200 and dead==0:
        print()
        print("You won the game!")
        print()
        done=True
    if random.randrange(0,20)==0 and dead==0 and choice!="e" and choice!="E" and choice!="q" and choice!="Q" and done!=True:
        print()
        print("You have found an oasis")
        print()
        drinks=5
        thirst=0
        tired=0