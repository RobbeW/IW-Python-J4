# Vraag een getal aan de gebruiker
kanaal = int(input("Geef het kanaalnummer in: " ) )
nieuw = int(input("Geef het aantal keer vooruit zappen in: "))

# Bereken het nieuwe kanaal
kanaal += nieuw

# Druk deze op het scherm af
print(f"Nieuwe kanaalnummer: {kanaal % 100}")
