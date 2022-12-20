import time

print("Finally Krampus is killed and all the fear is lost")
time.sleep(2)
keuze_zwaard = input("You are returning to the old monster, do you want to give him the sword back, [YES] or [NO]? ")
if keuze_zwaard == "yes":
    print("The sword is back with his original owner, you ask him the way back to the portal...")
    time.sleep(2)

elif keuze_zwaard == "no":
    print("You didn't give the sword back and asked the way back to the portal")
    time.sleep(3)
    print("Instead you put it later in your room so you will never forget")
    time.sleep(2)
    print("You went home and your mother opens the door and askes you where you were")

else:
    print("You didn't give him the sword back, instead, you bring it with you home and ask him the way back to the portal...")
    time.sleep(2)
    print("You woke up at the door, the door was already open and you walk in.")
    time.sleep(3)
    print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")

    # keuze1 = "I stayed overnight with a friend"
    # keuze2 = "I had to survive in the woods for school"
    # keuze3= "you say nothing and keep walking"

    # keuze_leugen = input("You have 3 options to choose of... \n[1]you can say you stayed with a friend, \n[2]survive in the woods for school or \n[3]you say nothing and keep walking")
    # if keuze_leugen == "1":
    #     print("your parents believe you but are a little stressed")
    # elif keuze_leugen == "2":
    #     print("")





    keuze_bedanken = input("Do you want to thank him that he give you his sword? [YES] or [NO]...")
    if keuze_bedanken == "yes":
        print("You thanked him very much and you go back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(3)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")
    elif keuze_bedanken == "no":
        print("You didn't thank him and got back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(3)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")

