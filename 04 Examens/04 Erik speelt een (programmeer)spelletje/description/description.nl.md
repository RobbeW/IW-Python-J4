## Gegeven
Bij Fizzbuzz vertrek je van een willekeurig getal en ga je zo snel mogelijk tot een eindgetal door elk getal hiertussen op te sommen. De moeilijkheid in dit spel is dat je alle veelvouden van 3 vervangt door “FIZZ” en alle veelvouden van 5 door “BUZZ”. 
Zo zijn de eerste 10 getallen niet gewoon: 
1, 2, 3, 4, 5, 6, 7, 8, 9 en 10 
Maar krijg je wel: 
1, 2, FIZZ, 4, BUZZ, FIZZ, 7, 8, FIZZ en BUZZ. 
Elk getal dat een veelvoud van zowel 3 als 5 is, wordt FIZZBUZZ.  

![Erik tijdens het programmeren.](media/programmeur.jpg "Erik tijdens het programmeren."){:data-caption="Erik tijdens het programmeren." width="45%"}

## Opgave
Schrijf een programma dat aan de gebruiker een begin- en eindgetal vraagt. Het programma zal alle getallen hiertussen overlopen en weergeven, tenzij het dus een veelvoud is van 3 en/of 5. 

Gebruik in je code de functies `veelvoud3(...)` en `veelvoud5(...)` om te controleren of het getal een veelvoud is van 3 of 5.  

#### Voorbeelden

Met begingetal `1` en eindgetal `10` krijgen we:
```
1
2
FIZZ
4
BUZZ
FIZZ
7
8
FIZZ
BUZZ
```


Met begingetal `15` en eindgetal `25` krijgen we:
```
FIZZBUZZ
16
17
FIZZ
19
BUZZ
FIZZ
22
23
FIZZ
BUZZ
```