termen = int(input("Hoeveel termen"))
uitkomst = 0
for i in range(termen):
    eersteGetal = (i + 1) * 2
    tweedeGetal = eersteGetal + 1
    derdeGetal = tweedeGetal + 1
    if i % 2 == 0:
        uitkomst += 1 / (eersteGetal * tweedeGetal * derdeGetal)
    else:
        uitkomst -= 1 / (eersteGetal * tweedeGetal * derdeGetal)
uitkomst = 3 + uitkomst * 4
print("De Nilakantha-benadering van pi met", termen,"termen is", round(uitkomst,6))