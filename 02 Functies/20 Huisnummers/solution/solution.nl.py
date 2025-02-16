def som_onder(nummer):
    som = 0
    for i in range(nummer):
        som += i
    return som

def is_symmetrisch(nummer):
    som = som_onder(nummer)
    flag = False
    nieuwe_som = 0
    while True:
        nummer += 1
        nieuwe_som += nummer
        if nieuwe_som == som:
            flag = True
        elif nieuwe_som > som:
            break
    
    return flag

# Invoer vragen
bovengrens = int(input("Geef een bovengrens in: "))

afgedrukt = False
for i in range(1, bovengrens + 1):
    if is_symmetrisch(i):
        afgedrukt = True
        print(i, "voldoet aan de bijzondere eigenschap.")

if not afgedrukt:
    print("Er waren geen nummers kleiner dan", bovengrens, "die hieraan voldoen.")