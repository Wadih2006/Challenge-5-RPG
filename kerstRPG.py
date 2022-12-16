import time 
import random
from art import *


klaar_knop = input("This game contains a scary story, make sure you play this in a safe place... (press any button) ")
klaar_knop = ()
print("Before we begin, a special thanks to Kevin & Wadih for making this game.")
print("Lets begin the story...")
time.sleep(3)
print("Prepare yourself😈...")
time.sleep(3)
print("CHAPTHER ONE: The House.")
time.sleep(3)
print("You're a boy named Griffin who is 17 years old. Everyday you go to school by train, you got bullied many times at school and run to the woods nearby, but the bully is running after you. You look back but then you hit a tree and fall unconscious.")
time.sleep(6)
print("You finally wake up in the \x1B[3m" + "christmas" + "\x1B[0m woods next to an old house.")
print("""\n        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~""")


keuze_huis = input("You decide to go check it... first the [INSIDE] or check the [OUTSIDE]?\n ")

if keuze_huis == "inside":
    print("You discide to check the inside.\n ")

elif keuze_huis == "outside":
    print("You are checking the outside and see a shed, you go in and see nerfguns laying on the table and pick them up... Then you go in the house...")

else:
    print("Give a good answer to continue.\n ")

    
keuze_buiten = input("You are inside and have the option to go [UPSTAIRS] or go to the [BASEMENT]...\n ")
if keuze_buiten == "upstairs":
    print("Once you go upstairs there is allot broken toys and ripped teddy bears,\n broken windows, floor and door that has scratches from big, long scary claws.\n You think this is scary, so you decide to go downstairs.")
    time.sleep(5)
    print("when you are at the main floor you really want to go home but...\n you know something strange is waiting for you in the basement.")
    time.sleep(4)
    print("you know you aren't prepaired for what's down there but you still go there...")
    time.sleep(4)
    print("you saw a portal standing in the middle of the basement\n you tried to turn it off but then you got sucked in...")
    
elif keuze_buiten == "basement":
    print("you know you aren't prepaired for what's down there but you still go there...")
    time.sleep(3)
    print("you saw a portal standing in the middle of the basement\n you tried to turn it off but then you got sucked in...")
   
   
    
print("NEW CHAPTER UNLOCKED: The Dark Night. ")

keuze_schuur = input("you wake up in an old shed and hear something whispering in the back of the shed.\n do you [ESCAPE]] or [STAY] and figure out what the sound is. ")
if keuze_schuur == "escape":
    print("you tried to escape from krampus but he was too fast for you so he killed you.")
    time.sleep(2)
    print("YOU DIED! try again. ")
    
elif keuze_schuur == "stay":
    print("once you found out there was no one whispering but speaking to himself you found out that there was an old slave of Krampus... ")
    time.sleep(4)
    print("He was trapped inside of a cage ")
    print("""\n
================================
||     ||<(.)>||<(.)>||     || 
||    _||     ||     ||_    || 
||   (__D     ||     C__)   || 
||   (__D     ||     C__)   ||
||   (__D     ||     C__)   ||
||   (__D     ||     C__)   ||
||     ||     ||     ||     ||
================================""")
    
    time.sleep(5)
    print("you tried to talk to him but he was to afraid to talk to you... ")
    time.sleep(3)
    print("it's been 20 minutes you tried to talk to him and out of a sudden he spoke \nand gave you all the information you needed to defeat Krampus and gave you his sword")
    time.sleep(5)
    print("he looked so hungry so you gave him something to eat that you have been stored in your pockets")
    time.sleep(4)
    print("""\n
    __________________,.............,    
   /_/_/_/_/_/_/_/_/,-',  ,. -,-,--/|
  /_/_/_/_/_/_/_/,-' //  /-| / /--/ /
 /_/_/_/_/_/_/,-' `-''--'  `' '--/ /
/_/_/_/_/_/_,:................../ /
|________,'                     |/
         """"""""""""""""""""""")
    
    print("you are thinking of trying to free him but that's really dangerous if Krampus finds out you're dead so make the right choice...")
    gelukkooi = input("you try to brake the cage open but if Krampus hears this then you're dead [PRESS ENTER TO SEE IF IT WORKED]")

keuze_bevrijden = random.randint(1, 10)

if keuze_bevrijden <= 3:
    print("Krampus killed you!")

else:
    print("you freed the old slave!")
    
    
schuur_bevrijding = print("you did free him so now he opened the door of the shed to the forest so you could hunt for Krampus and free all the children he kidnapped.")
time.sleep(5)
print("you walked through the scary dark lurid forest. it was so dark you couldn't even see anything")
time.sleep(4)
print("Suddenly you heard something rustle behind you...")
keuze_forest = input("do you want to [CHECK] it or [IGNORE] it? ")
if keuze_forest == "check":
    print("you looked for a couple of minutes but you did not found something so you walked further.")
    
else:
    print("you ignored the sound so you walked furhter.")

time.sleep(4)
print("you heard the sound again but this time it was way scarier.")
time.sleep(4)
print("the sound sounded like someone was dying of pain and someone else was crying...")



