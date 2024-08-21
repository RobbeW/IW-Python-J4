def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal

# invoer vragen
bovengrens = int(input("Geef een bovengrens in: " ))

# priemtweelingen afdrukken
for i in range(2, bovengrens):
    if i == 2:
        print("2 is een geïsoleerd priemgetal.")
    elif is_priem(i) and not is_priem(i - 2)  and not is_priem(i + 2) :
        print(i, "is een geïsoleerd priemgetal.")
