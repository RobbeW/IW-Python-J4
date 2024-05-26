def groter_dan( lijst, getal ):
    n = len(lijst)
    aantal = 0
    for i in range(n):
        if lijst[i] > getal:
            aantal += 1
            print(f"Op plaats {i} staat een getal groter dan {getal}")
    return aantal
