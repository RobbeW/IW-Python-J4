## Gegeven
Erik kijkt, naast zijn verjaardagsfeest, ook al enorm uit naar de grote vakantie. Hij gaat zijn leerkrachten enorm missen gedurende twee maanden, maar om zijn gedachten te kunnen verzetten, gaat hij met zijn ouders op vakantie naar Italië. 

De ouders van Erik zijn echter nog in twijfel of ze samen met hun enige zoon het vliegtuig nemen of met de auto gaan. Vooral aangezien ze daar ook graag met een auto willen rondrijden. 

![Vervoersmiddel voor de reis.](media/vakantie_voertuig.jpg "Vervoersmiddel voor de reis."){:data-caption="Vervoersmiddel voor de reis." width="45%"}

## Opgave
Schrijf een programma om de ouders te helpen bij dit probleem en op basis van de (gereden) afstand te bepalen welke optie hen het voordeligst uitkomt. Je zal hiervoor rekening moeten houden met: het verbruik van het vliegtuig, het huren van een auto en het verbruik van de eigen / gehuurde auto per gereden kilometer. 

Schrijf hiervoor 2 functies:
- De functie `kostAuto(...)` berekent de kost (in euro) van het rijden met een auto aan 15 cent per gereden kilometer. 
- De functie `kostVliegen(...)` berekent de totaalprijs van de vliegvakantie op basis van de vlucht (€30 **per persoon** per 1000 kilometer), de huurprijs van de auto (€100 startprijs) en de gereden afstand met deze auto. **Maak voor dit laatste stuk dus gebruik van de vorige functie**.

Schrijf hierna een programma dat aan de gebruiker vraagt hoe ver de vakantiebestemming ligt (in km) en hoe veel km het gezin nog wil rondrijden op de bestemming. Het programma berekent daarna welke optie er goedkoper is en hoeveel ze daarmee besparen.

#### Voorbeelden

Met Rome als reisbestemming op (ongeveer) `1500` km afstand, waarna het gezin nog `100` km wil rondrijden om de rest van Italië te bezoeken krijgen we:
```
Je gaat beter met het vliegtuig, je bespaart dan € 80.0.
```


Met Amsterdam als reisbestemming op (ongeveer) `200` km afstand, waarna het gezin voornamelijk binnenin de stad blijft en dus slechts `20` km rondrijdt krijgen we:
```
Je gaat beter met de auto, je bespaart dan € 76.0.
```

{: .callout.callout-info}
> #### Tips
> - Als je naar een bestemming op vakantie gaat moet je natuurlijk ook **terug naar België**. Vergeet de reisafstand dus niet te verdubbelen.