def aantal_tussen(lijst, a, b):
    n = len(lijst)
    aantal = 0
    for getal in lijst:
        if a <= getal <= b:
            aantal += 1
    return aantal
