def aqi(ozon, nitro):
    eAQI = 0
    if ozon >= 380 or nitro > 340:
        eAQI = 6
    elif ozon >= 240 and ozon < 380 or nitro >= 230 and nitro < 340:
        eAQI = 5
    elif ozon >= 130 and ozon < 240 or nitro >= 120 and nitro < 230:
        eAQI = 4
    elif ozon >= 100 and ozon < 130 or nitro >= 90 and nitro < 120:
        eAQI = 3
    elif ozon >= 50 and ozon < 100 or nitro >= 40 and nitro < 90:
        eAQI = 2
    else:
        eAQI = 1
    return eAQI

# Vraag invoer
ozon = int(input("Geef het meetresultaat voor ozon in µg/m³: "))
nitro = int(input("Geef het meetresultaat voor stikstofdioxide in µg/m³: "))

index = aqi(ozon, nitro)

# Weergave
print("Europese AQI:", index)
