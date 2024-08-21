def oppervlakte_veelhoek(x, y):
    n = len(x)
    deel1 = 0
    deel2 = 0
    for i in range(n):
        deel1 += x[i]*y[(i + 1) % n]
        deel2 += y[i]*x[(i + 1) % n]
    
    A = 0.5 * abs(deel1 - deel2)
    return round(A, 2)
