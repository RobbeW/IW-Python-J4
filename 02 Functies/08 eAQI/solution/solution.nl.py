def eAQI(ozon, nitro):
    if ozon < 50:
        index_o = 1
    elif ozon < 100:
        index_o = 2
    elif ozon < 130:
        index_o = 3
    elif ozon < 240:
        index_o = 4
    elif ozon < 380:
        index_o = 5
    else:
        index_o = 6
        
    if nitro < 40:
        index_n = 1
    elif nitro < 90:
        index_n = 2
    elif nitro < 120:
        index_n = 3
    elif nitro < 230:
        index_n = 4
    elif nitro < 340:
        index_n = 5
    else:
        index_n = 6
    
    return max(index_o, index_n)

# Vraag invoer
ozon = int(input("Geef het meetresultaat voor ozon in µg/m³: "))
stikstofdioxide = int(input("Geef het meetresultaat voor stikstofdioxide in µg/m³: "))

# Functie testen
index = eAQI(ozon, stikstofdioxide)

# Weergave
print(f"Europese AQI: {index}")
