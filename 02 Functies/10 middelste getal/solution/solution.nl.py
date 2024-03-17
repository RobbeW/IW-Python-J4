def midden( a, b, c ):
    maximum = max(a,b,c)
    minimum = min(a,b,c)
    
    result = (a+b+c) - maximum - minimum
    return result

# Invoer vragen
a = int(input())
b = int(input())
c = int(input())

# Verwerking
m = midden(a,b,c)

# Uitvoer
print(f"Het middelste getal was: {m}")
