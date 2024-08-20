# Invoer van de uren, minuten en seconden
u = int( input( "Geef het uur in: " ) )
m = int( input( "Geef de minuten in: " ) )

# Invoer en omrekenen van de offset
offset = float( input( "Geef de toename of afname in aantal uren in: " ) )
offset_min = int( offset * 3600 )

# Berekeningen
time = u * 3600 + m * 60
time += offset_min

u_new = ( time // 3600 ) % 24
m_new = ( time % 3600 ) // 60

# Weergave
print("Het is", u_new, "uur en", m_new, "minuten in de andere tijdzone.")

