def aqi(ozon, nitro):
    eAQI = 0
    if ozon >= 380 or stikstofdioxide > 340:
        eAQI = 6
    elif ozon >= 240 and ozon < 380 or stikstofdioxide >= 230 and stikstofdioxide < 340:
        eAQI = 5
    elif ozon >= 130 and ozon < 240 or stikstofdioxide >= 120 and stikstofdioxide < 230:
        eAQI = 4
    elif ozon >= 100 and ozon < 130 or stikstofdioxide >= 90 and stikstofdioxide < 120:
        eAQI = 3
    elif ozon >= 50 and ozon < 100 or stikstofdioxide >= 40 and stikstofdioxide < 90:
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
