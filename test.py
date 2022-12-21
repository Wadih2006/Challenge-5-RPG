import random

keuze_bevrijden = random.randint(1, 10)

if keuze_bevrijden <= 3:
    print("Krampus killed you!")
    exit()
else:
    print("You freed the old slave!")