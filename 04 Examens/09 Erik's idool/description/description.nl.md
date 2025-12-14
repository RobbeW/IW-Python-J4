## Gegeven
Erik heeft een groot idool. Nilakantha was een wiskundige en astronoom die leefde tijdens de 15e eeuw. Hij kwam uit India en schreef onder andere het boek *Tantrasangraha*, waarin meerdere voorbeelden van wiskunde, die (voor die tijd) zeer geavanceerd waren, stonden. In dit boek stond er ook een reeks om het getal **pi** te kunnen benaderen.

![Erik's idool Nilakantha.](media/nilakantha.jpg "Erik's idool Nilakantha."){:data-caption="Erik's idool Nilakantha." width="45%"}

De benadering werkte als volgt:

$$
\mathsf{\dfrac{\pi - 3}{4} = \dfrac{1}{2 \cdot 3 \cdot 4} - \dfrac{1}{4 \cdot 5 \cdot 6} + \dfrac{1}{6 \cdot 7 \cdot 8} - \dfrac{1}{8 \cdot 9 \cdot 10} + \ldots}
$$

Je kan deze uitdrukking omvormen om de waarde van π te berekenen (in de praktijk: *benaderen*)

$$
\mathsf{\pi = 3 + 4 \cdot \left( \dfrac{1}{2 \cdot 3 \cdot 4} - \dfrac{1}{4 \cdot 5 \cdot 6} + \dfrac{1}{6 \cdot 7 \cdot 8} - \dfrac{1}{8 \cdot 9 \cdot 10} + \ldots \right)}
$$

## Opgave
Bepaal een benadering voor het getal π met bovenstaande uitdrukking. Schrijf een programma dat naar het aantal termen vraagt en vervolgens via een begrensde herhaling de benadering uitrekent. Rond de benadering af op **6 cijfers na de komma**.


#### Voorbeelden

Indien de gebruiker `2` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{3 + 4 \cdot \left(\dfrac{1}{2 \cdot 3 \cdot 4} - \dfrac{1}{4 \cdot 5 \cdot 6}\right ) \approx 3,133333\ldots}
$$

Zodat er verschijnt:
```
De Nilakantha-benadering van pi met 2 termen is 3.133333
```


Indien de gebruiker `5` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{3 + 4 \cdot \left(\dfrac{1}{2 \cdot 3 \cdot 4} - \dfrac{1}{4 \cdot 5 \cdot 6} + \dfrac{1}{6 \cdot 7 \cdot 8} - \dfrac{1}{8 \cdot 9 \cdot 10} + \dfrac{1}{10 \cdot 11 \cdot 12} \right ) \approx 3,142713\ldots}
$$

Zodat er verschijnt:
```
De Nilakantha-benadering van pi met 5 termen is 3.142713
```