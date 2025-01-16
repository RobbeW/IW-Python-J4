Een silo begint met een grote voorraad graan. Elke dag wordt een vaste hoeveelheid graan uit de silo gehaald om vee te voeden. Het is bijna oogsttijd. Elke dag wordt een hoeveelheid graan aan de silo toegevoegd. Er is een starthoeveelheid en deze neemt elke dag toe met een vaste hoeveelheid.

![Foto door Chris Robert op Unsplash.](media/chris-robert.jpg "Foto door Chris Robert op Unsplash."){:data-caption="Foto door Chris Robert op Unsplash." width="40%"}

Het doel van deze oefening is om de voorraad bij te houden en het laagste punt te detecteren.

## Opgave
Schrijf een programma dat de **startvoorraad** graan (in kg) vraagt. Daarna vraag je het aantal kg dat dagelijks **uit** de silo gehaald wordt als veevoeder.

Vraag nadien met hoeveel kg graan, uit de oogst, de graansilo **aangevuld** wordt. En met welke hoeveelheid deze aanvulling elke dag stijgt.

Berekent tot slot de **kleinste hoeveelheid** graan in de silo en geeft dit weer. Geef ook alle tussentijdse hoeveelheden weer. Bestudeer grondig onderstaand voorbeeld.

#### Voorbeeld
Stel dat de silo reeds `5000` kg graan bevat. Het vee wordt elke dag met `200` kg graan gevoederd. Er wordt de eerste dag slechts `125` kg graan geoogst. Maar deze hoeveelheid stijgt elke dag met `50` kg. Dan verschijnt er:

```
Na dag 1 bevat de silo 4925 kg graan.
Na dag 2 bevat de silo 4900 kg graan.
De silo bevatte het minste graan na 2 dagen, namelijk 4900 kg.
```

De eerste dag bereken je de hoeveelheid graan immers via: 5000 kg - 200 kg + 125 kg = 4925 kg. De volgende dag wordt er 50 kg meer geoogst, dus in het totaal komt er 175 kg bij. De berekening de volgende dag is bijgevolg 4925 kg - 200 kg + 175 kg = 4900 kg. De volgende dag zal er 225 kg geoogst worden, men berekent nu 4900 kg - 200 kg + 225 kg = 4925 kg. 

Men merkt dus op dat de hoeveelheid graan minimaal was na 2 dagen, namelijk 4900 kg.
