import time

print("Finally Krampus is killed and all the fear is lost")
time.sleep(2)
keuze_zwaard = input("You are returning to the old monster, do you want to give him the sword back, [YES] or [NO]?" )
if keuze_zwaard == "yes":
    print("The sword is back with his original owner, you ask him the way back to the portal...")
    time.sleep(4)
    keuze_bedanken = input("Do you want to thank him that he give you his sword? [YES] or [NO]..." )
    if keuze_bedanken == "yes":
        print("You thanked him very much and you go back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(5)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")
    elif keuze_bedanken == "no":
        print("You didn't thank him and got back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(5)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")
else:
    print("You didn't give him the sword back, instead, you bring it with you home and want to put it in your room. You asked him the way back to the portal...")
    time.sleep(7)
    print("You go home and your mother was waiting at the door to asks you where you have been.")
    time.sleep(4)
    keuze_leugen = input("[1]I stayed overnight with a friend, [2]I had to survival in the woods for school, [3]You say nothing and walks further..." )
    if keuze_leugen == "1":
        print("Your parents believe you but are a little bit stressed")
        time.sleep(3)
    elif keuze_leugen == "2":
        print("Your parents don't believe this and call your school to ask")
        time.sleep(3)
        print("To be continued...")
        time.sleep(3)
    elif keuze_leugen == "3":
        print("Your mother calls the police to ask if they know anything about this")
        time.sleep(3)
        print("To be continued...")
        time.sleep(3)
    print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")