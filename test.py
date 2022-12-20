import time

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
    time.sleep(4)
    
elif aanval_guard == "calves":
    print("it doesn't do anything to he laughs at you and kill you...")
    time.sleep(4)
    print("you died! try again.")
    
else:
    print("give a good answer. ")
    exit()

print("you killed the monster correcly. congratulations!")
time.sleep(3)
print("luckily the last one had the keys from the cage of the children... ")
time.sleep(3)
print("all out of a sudden he heard a kid scream he was so scared because he knew he could go in prison for killing someone.")
time.sleep(5)
print("he was so brave that he got to the room where the children have been trapped.")
time.sleep(4)
print("you opened the door and saw a huge cage where the kids have been trapped in.")