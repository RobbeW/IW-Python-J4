import math

def minimum_sonar(n, m):
    x = math.ceil((n - 2) / 3)
    y = math.ceil((m - 2) / 3)
    return x * y
