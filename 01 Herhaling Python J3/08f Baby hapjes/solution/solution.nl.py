# Vraag naar het aantal hapjes
n = int(input("Geef het aantal hapjes in: "))

is_correct = True
# Herhaling
for i in range(n):
    baby = input("Geef het antwoord van de baby in: ")
    if baby != "gemompel":
        if int(baby) != i + 1:
            is_correct = False

# Uiteindelijke print
if is_correct:
    print("Dit lijkt te kloppen.")
else:
    print("Hier klopt iets niet...")
