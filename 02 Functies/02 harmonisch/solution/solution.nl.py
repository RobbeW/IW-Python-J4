def harmonisch_gemiddelde( a, b ):
    harm_mean = round( 2 / ( 1 / a + 1 / b ), 2)
    return harm_mean 

# Gegevens vragen
a = int(input())
b = int(input())

# Harmonishc gemiddelde berekenen
c = harmonisch_gemiddelde(a,b)

# Weergeven op het scherm
print(f"Het harmonisch gemiddelde van {a} en {b} is {c}")

