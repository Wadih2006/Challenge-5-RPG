import time 
from art import *


klaar_knop = input("this game contains a scary story make sure you play this in a safe place... (press any button) ")
klaar_knop = ()
print("before we begin a special thanks to Kevin & Wadih for making this game")
print("lets begin the story...")
time.sleep(3)
print("you're a boy named Griffin who is 17 years old. you got bullied in the woods and have fallen unconscious.")
time.sleep(3)
print("you suddenly wake up in the Christmas woods next to an old house.")
print("""\n        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~""")


keuze_huis = input("you decide to go check it... first the [INSIDE] or check the [OUTSIDE] ")

if keuze_huis == "inside":
    print("you discide to check the inside. ")

elif keuze_huis == "outside":
    print("when you checked the outside there is a shed. there are nerf guns laying on a table, you pick them up...")

else:
    print("give a good answer to continue. ")
    
    
keuze_buiten = input("then you go inside and have the option to go [UPSTAIRS] or go to the [BASEMENT]... ")
if keuze_buiten == "upstairs":
    print("once you go upstairs there is allot broken toys and ripped teddy bears,\n broken windows, floor and door that has scratches from big, long scary claws.\n You think this is scary, so you decide to go downstairs.")
    time.sleep(5)
    print("when you are at the main floor you really want to go home but...\n you know something strange is waiting for you in the basement.")