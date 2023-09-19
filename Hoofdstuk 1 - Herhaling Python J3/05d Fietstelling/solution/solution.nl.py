# Invoer
snelheid_m_per_sec = float( input( "Geef een snelheid in: " ) )

# Omvormen naar km/u
snelheid = snelheid_m_per_sec / 1000 * 3600

# Verwerking en uitvoer
if snelheid >= 50:
    print( "Deze persoon fietst te snel, er volgt een boete." )
elif snelheid > 36:
    print( "Deze persoon fietst waarschijnlijk met een speedpedelec." )
elif snelheid < 25:
    print( "Dit is waarschijnlijk een reguliere fietser." )
else:
    print( "Het gaat hier waarschijnlijk om een (lichte) e-bike.")
