# Invoer
dosis = float(input("Geef de begindosis in: "))

# Berekening
i = 0
vorige = dosis - 1
while abs(vorige - dosis) >= 0.01:
    vorige = dosis
    i += 1
    dosis = dosis / 2 + 0.3
    print("Na dag", i, "is er", round(dosis, 4), "ml Ciloxan in het bloed.")

# Weergave
if i == 1:
    print("Na één dag was de concentratie Ciloxan al stabiel.")
else:
    print("Na", i, "dagen was de concentratie Ciloxan stabiel.")
