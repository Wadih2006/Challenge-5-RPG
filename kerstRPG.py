import time 
import random
# from art import *


klaar_knop = input("This game contains a scary story, make sure you play this in a safe place... (press enter to continue) ")
klaar_knop = ()
print("Before we begin, a special thanks to Kevin & Wadih for making this game.")
print("Lets begin the story...")
time.sleep(3)
print("Prepare yourself😈...")
time.sleep(3)
print("CHAPTHER ONE: The House.")
time.sleep(3)
print("You're a boy named Griffin who is 17 years old. You go to school by train everyday, you got bullied many times at school and run to the woods nearby, but the bully is running after you. You look back but then you hit a tree and fall unconscious.")
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
    print("When you are at the main floor you really want to go home, but...\n you know something strange is waiting for you in the basement.")
    time.sleep(4)

elif keuze_buiten == "basement":
    print("You know you aren't prepaired for what's down there but you still go there...")
    time.sleep(4)
    print("You saw a portal floating in the middle of the basement\n you tried to turn it off but then you got sucked in...")
        
print("NEW CHAPTER UNLOCKED: The Dark Night. ")

keuze_schuur = input("You wake up in an old shed and hear something whispering in the back of the shed.\n do you [ESCAPE] or [STAY] and figure out what the sound is. ")
if keuze_schuur == "escape":
    print("You tried to escape from krampus but he was too fast for you so...")
    time.sleep(2)
    print("YOU DIED! try again. ")
    
elif keuze_schuur == "stay":
    print("Once you found out there was no one whispering but speaking to himself you found out that there was an old slave of Krampus... ")
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
    print("You tried to talk to him but he was to afraid to talk to you... ")
    time.sleep(3)
    print("It's been 20 minutes you tried to talk to him and out of a sudden he spoke \nand gave you all the information you needed to defeat Krampus and gave you his sword")
    time.sleep(5)
    print("He looked so hungry so you gave him something to eat that you have been stored in your pockets")
    time.sleep(4)
    print(r"""\n
  ___  ___  ___  ___  ___.---------------.
.'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \
|\/ __\/ __\/ __\/ __\/ _:\   |`.  \  \___ \
 \\'\__\'\__\'\__\'\__\'\_`.__|""`. \  \___ \
  \\/ __\/ __\/ __\/ __\/ __:                \
   \\'\__\'\__\'\__\ \__\'\_;-----------------`
    \\/   \/   \/   \/   \/ :                 |
     \|______________________;________________|""")
    
    print("You are thinking of trying to free him but that's really dangerous if Krampus finds out you're dead so make the right choice...")
    gelukkooi = input("you try to brake the cage open but if Krampus hears this then you're dead [PRESS ENTER TO SEE IF IT WORKED]")

keuze_bevrijden = random.randint(1, 10)

if keuze_bevrijden <= 3:
    print("Krampus killed you!")
    exit()
else:
    print("You freed the old slave!")
    
    
schuur_bevrijding = print("You did free him so now he opened the door of the shed to the forest so you could hunt for Krampus and free all the children he kidnapped.")
time.sleep(5)
print("You walked through the scary dark lurid forest. It was so dark you couldn't even see anything")
time.sleep(4)
print("Suddenly you heard something rustle behind you...")
keuze_forest = input("do you want to [CHECK] it or [IGNORE] it? ")
if keuze_forest == "check":
    print("You looked for a couple of minutes but you did not found something so you walked further.")
    
else:
    print("you ignored the sound so you walked furhter.")

time.sleep(4)
print("You heard the sound again but this time it was way scarier.")
time.sleep(4)
print("the sound sounded like someone was dying of pain and someone else was crying...")
time.sleep(4)
print("you're brave enough to check the sound out. but then suddenly you found a map. ")
time.sleep(4)
print("a map leading to a huge house from Krampus where the kids have been trapped.")
time.sleep(4)
print("he was scared but brave enough to take a run to the house")
time.sleep(4)
print("you have arrived at the huge house")
print("NEW CHAPTER UNLOCKED: Kids House.")
time.sleep(4)
print(r"""                        
                                  {} {}
                            !  !  II II  !  !
                         !  I__I__II II__I__I  !
                         I_/|--|--|| ||--|--|\_I
        .-'"'-.       ! /|_/|  |  || ||  |  |\_|\ !       .-'"'-.
       /===    \      I//|  |  |  || ||  |  |  |\\I      /===    \
       \==     /   ! /|/ |  |  |  || ||  |  |  | \|\ !   \==     /
        \__  _/    I//|  |  |  |  || ||  |  |  |  |\\I    \__  _/
         _} {_  ! /|/ |  |  |  |  || ||  |  |  |  | \|\ !  _} {_
        {_____} I//|  |  |  |  |  || ||  |  |  |  |  |\\I {_____}
   !  !  |=  |=/|/ |  |  |  |  |  || ||  |  |  |  |  | \|\=|-  |  !  ! 
  _I__I__|=  ||/|  |  |  |  |  |  || ||  |  |  |  |  |  |\||   |__I__I_
  -|--|--|-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |--|--|-
  _|__|__|   ||_|__|__|__|__|__|__|| ||__|__|__|__|__|__|_||-  |__|__|_
  -|--|--|   ||-|--|--|--|--|--|--|| ||--|--|--|--|--|--|-||   |--|--|- 
   |  |  |=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  | 
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |  |  | 
   |  |  |-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  | 
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |  |  |
   |  |  |=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |  |  |
   |  |  |   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||-  |  |  |
  _|__|__|   || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||=  |__|__|_
  -|--|--|=  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||   |--|--|-
  _|__|__|   ||_|__|__|__|__|__|__|| ||__|__|__|__|__|__|_||-  |__|__|_
  -|--|--|=  ||-|--|--|--|--|--|--|| ||--|--|--|--|--|--|-||=  |--|--|-
  -|--|--|-  || |  |  |  |  |  |  || ||  |  |  |  |  |  | ||-  |  |  |
 ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~""")
print("you opened the old gate.")
time.sleep(4)
print("when you opened it it sounded like someone was screaming... just like when you were walking in the woods")
time.sleep(5)
print(r"""
                               .     .
                               !!!!!!!
                       .       [[[|]]]    .
                       !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\-_--\
               |=|    /-_---__/__-__-_\__-_\
           . . |=| ._/-__-__\===========/-__\_
           !!!!!!!!!\========[ /]]|[[\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\ ||== =|
        /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\===========/-----/
   ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
       ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
      _||_ = =||o---.|| = ==_||_= == =||==_||_
      \__/= = ||:   :||= == \__/[][][][][]\__/
      [||]= ==||:___:|| = = [||]\\//\\//\\[||]
      }  {---'"'-----'"'- --}  {//\\//\\//}  {
    __[==]__________________[==]\\//\\//\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
   |^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
 \\///\\\//===============\\//\\///\\\\////\\\/////
 """)
print("it was big, scary, dark, creepy and there were broken toys and teddy bears… also there was scuffed furniture in front of the house")
time.sleep(6)
print("you went in quickly. actually broken into")
time.sleep(3)
print("there he was... Krampus.")
time.sleep(2)
keuze_verstoppen = input("you had the choice to hide under the [FURNITURE] or act like a [DOLL] standing in the hallway. ")
if keuze_verstoppen == "furniture":
    print("you hid under the furniture and table. luckily he didn't see you.")
    
else:
    print("you tried to act like a doll standing in the hallway. he did saw you and ripped you apart (try again!)")
    exit()
print("the hall in front of the room with children there where so many guards")
time.sleep(4)

keuze_aanval = input("You had the option to go [AGRESSIVE MODE] or [STEALTH MODE]")
if keuze_aanval == "agressive mode":
    print("You are fighting now aggresive against the guardiens and kill all of them, but you can get hurt")
else:
    print("You are sneeking really silent and kill the guardien infront of the cage")
    time.sleep(3)
    print("He has the keys to the cage where the kids are trapped in.")




print("You freed the kids, but Krampus is comming and you put the kids in a box.")
time.sleep(3)
keuze_verstoppen = input("You hide them under the [TABLE] or under the [MACHINE]...")
if keuze_verstoppen == "table":
    print("You have hidden the kids under, but Krampus is comming and you have to fight him")
else:
    print("You have hidden the kids under, but Krampus is comming and you have to fight him")

time.sleep(3)
print("When you want to fight Krampus, you suddenly find a Nerf RPG that was left from the kids. You allready had bullets that you find outside and reload the Nerf RPG")
time.sleep(3)
keuze_aanvallen = input("The sword that you have are going to [ATTACH] to the Nerf RPG or you [SHOOT] with the Nerf RPG...")
if keuze_aanvallen == "attach":
    print("The sword is attached to the Nerf RPG and attack him")
    time.sleep(3)
    print("He is really injured and you finally kill him!!")
else:
    print("Use all the bullets you have against krampus")
    time.sleep(2)
    print("He falls on the ground and you finish him with your last attack!!")


print("Finally Krampus is killed and all the fear is lost")
time.sleep(2)
keuze_zwaard = input("You are returning to the old monster, do you want to give him the sword back, [YES] or [NO]?")
if keuze_zwaard == "yes":
    print("The sword is back with his original owner, you ask him the way back to the portal...")
    time.sleep(2)
    keuze_bedanken = input("Do you want to thank him that he give you his sword? [YES] or [NO]...")
    if keuze_bedanken == "yes":
        print("You thanked him very much and you go back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(3)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")
    elif keuze_bedanken == "no":
        print("You didn't thank him and got back home. You woke up at the door, the door was already open and you walk in.")
        time.sleep(3)
        print("\nThat is the end of the RPG, thanks to Kevin Simon & Wadih Ibrahim")
else:
    print("You didn't give him the sword back, instead, you bring it with you home and want to put it in your room. You asked him the way back to the portal...")
    time.sleep(2)
    print("You go home and your mother was waiting at the door and asks you where you have been.")
    time.sleep(2)
    keuze_leugen = input("[1]I stayed overnight with a friend, [2]I had to survival in the woods for school, [3]You say nothing and walks further...")
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