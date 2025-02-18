def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    # Indien geen delers werden gevonden is i == getal
    return i == getal


getal = int(input("Geef een getal in: "))

if getal % 2 != 0 or getal <= 2:
    print("Het vermoeden is hier niet van toepassing.")
else:
    for a in range(2, getal // 2 + 1):
        for b in range(getal // 2, getal):
            if a + b == getal and is_priem(a) and is_priem(b):
                print(a, "+", b, "=", getal)