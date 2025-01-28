import math

def minimum_sonar(n, m):
    x = math.ceil((n - 2) / 3)
    y = math.ceil((m - 2) / 3)
    return x * y


aantal_rijen = int(input("Geef het aantal rijen in: "))
aantal_kolommen = int(input("Geef het aantal kolommen in: "))

minimale_aantal = minimum_sonar(aantal_rijen, aantal_kolommen)

if minimale_aantal == 1:
    print("Er is minimaal 1 sonar nodig.")
else:
    print("Er zijn minimaal", minimale_aantal, "aantal sonars nodig.")
