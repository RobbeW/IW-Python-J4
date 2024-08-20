# Invoer
dosis = float(input("Geef de begindosis in: "))

# Berekening
i = 0
while True:
    i += 1
    nieuw = dosis / 2 + 0.3
    print("Na dag", i, "is er", round(nieuw, 4), "ml Ciloxan in het bloed.")
    
    if abs(nieuw - dosis) < 0.01:
        break
    dosis = nieuw

# Weergave
if i == 1:
    print("Na één dag was de concentratie Ciloxan al stabiel.")
else:
    print("Na", i, "dagen was de concentratie Ciloxan stabiel.")
