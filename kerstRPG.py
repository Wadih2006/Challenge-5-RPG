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

keuze_aanval = input("You had the option to go [AGRESSIVE MODE] or [SILENT MODE]. ")
if keuze_aanval == "agressive mode":
    print("You are fighting now aggresive against the guardiens")

elif keuze_aanval == "silent mode":
    print("you try to sneak past all guard and only kill the last. ")
    time.sleep(3)
    print(r"""         ,     .
        /(     )\               A
   .--.( `.___.' ).--.         /_\
   `._ `%_&%#%$_ ' _.'     /| <___> |\
      `|(@\*%%/@)|'       / (  |L|  ) \
       |  |%%#|  |       J d8bo|=|od8b L  <------ HEAD
        \ \$#%/ /        | 8888|=|8888 |
        |\|%%#|/|        J Y8P"|=|"Y8P F
        | (.".)%|         \ (  |L|  ) /
    ___.'  `-'  `.___      \|  |L|  |/
  .'#*#`-       -'$#*`.       / )|
 /#%^#%*_ *%^%_  #  %$%\    .J (__)
 #&  . %%%#% ###%*.   *%\.-'&# (__)
 %*  J %.%#_|_#$.\J* \ %'#%*^  (__)       <------ RIBS
 *#% J %$%%#|#$#$ J\%   *   .--|(_)
 |%  J\ `%%#|#%%' / `.   _.'   |L|
 |#$%||` %%%$### '|   `-'      |L|
 (#%%||` #$#$%%% '|            |L|
 | ##||  $%%.%$%  |            |L|
 |$%^||   $%#$%   |            |L|        <------ STOMACH
 |&^ ||  #%#$%#%  |            |L|
 |#$*|| #$%$$#%%$ |\           |L|
 ||||||  %%(@)$#  |\\          |L|
 `|||||  #$$|%#%  | L|         |L|
      |  #$%|$%%  | ||l        |L|        <------ LEGS
      |  ##$H$%%  | |\\        |L|
      |  #%%H%##  | |\\|       |L|
      |  ##% $%#  | Y|||       |L|
      J $$#* *%#% L  |E/
      (__ $F J$ __)  F/
      J#%$ | |%%#%L
      |$$%#& & %%#|                       <------ CALVES
      J##$ J % %%$F
       %$# * * %#&
       %#$ | |%#$%
       *#$%| | #$*
      /$#' ) ( `%%\
     /#$# /   \ %$%\
    ooooO'     `Ooooo
 """)
time.sleep(4)
print("the last guard is in front of you...")
time.sleep(3)
aanval_guard = input("what are you going to hit? his [HEAD] [RIBS] [STOMACH] [LEGS] or the [CALVES] ")
if aanval_guard == "head":
    print("you hit him on his head and the head falls off. ")
    time.sleep(4)
    print("but he continues the fight but he can't see anything so easy game and you finish him off.")
    
elif aanval_guard == "ribs":
    print("you hit him in his stomach and he istantly died.")

elif aanval_guard == "stomach":
    print("you hit him in his stomach and continued the fight... eventually you finished him.")
    time.sleep(4)
    print("WARNING! you are injured too.")
    
elif aanval_guard == "legs":
    print("you slice the sword trough his legs. they got cut off.")
    time.sleep(4)
    print("he can't walk anymore...")
    time.sleep(4)
    print("you can kill him really easy.")
    
elif aanval_guard == "calves":
    print("it doesn't do anything to he laughs at you and kill you...")
    time.sleep(4)
    print("you died! try again.")
    
else:
    print("give a good answer. ")
    exit()

print("luckily the last one had the keys from the cage of the children... ")
time.sleep(3)
print("all out of a sudden he heard a kid scream he was so scared because he knew he could go in prison for killing someone.")
time.sleep(5)
print("he was so brave that he got to the room where the children have been trapped.")
time.sleep(4)
print("you opened the door and saw a huge cage where the kids have been trapped in.")
time.sleep(4)
print()