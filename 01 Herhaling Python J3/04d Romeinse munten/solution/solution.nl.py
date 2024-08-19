# Invoer
bedrag = int(input("Geef het aantal nummus in: "))

# Verwerking
aantal_soldini = bedrag // 7200
rest = bedrag % 7200

aantal_miliarense = rest // 600
rest = rest % 600

aantal_siliqua = rest // 300
aantal_nummi = rest % 300

# Uitvoer
print(f"soldinus: {aantal_soldini}")
print(f"miliarense: {aantal_miliarense}")
print(f"siliqua: {(aantal_siliqua)}")
print(f"nummus: {aantal_nummi}")
