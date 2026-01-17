import math

def is_priem(getal):
    i = 2
    while i < getal and getal % i != 0:
        i = i + 1
    return i == getal

