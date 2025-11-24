aantal = int(input("Vul een aantal termen in: "))  

som = 0 
for i in range(aantal): 
    som += (-1)**i / (i * 2 + 1) 

print("De Leibniz-benadering van pi met", aantal, "termen is", round(som * 4, 6))