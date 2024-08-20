Windkracht wordt uitgedrukt in de <a href="https://nl.wikipedia.org/wiki/Schaal_van_Beaufort" target="_blank">schaal van Beaufort</a>. Oorspronkelijk telde de schaal 13 waarden, maar sinds 1946  werd een nieuwe schaal ontwikkeld die 17 waarden telt. Men berekent de Beaufort windsnelheid $$B$$ via de volgende formule:

$$
    B = \left(\dfrac{v}{0,836}\right)^\dfrac{2}{3}
$$

Hierbij wordt de Beaufort windsnelheid steeds afgerond op **eenheden** nauwkeurig en is $$v$$ uitgedrukt in $$\dfrac{\text{m}}{\text{s}}$$.

![Een windsok op het Nederlands strand.](media/beaufort.jpg "Foto door RoonZ nl op Unsplash."){:data-caption="Een windsok op het Nederlands strand." width="40%"}

## Opgave
Schrijf een programma dat de windsnelheid $$v$$ in $$\dfrac{\text{km}}{\text{u}}$$ vraagt en vervolgens de Beaufort windsnelheid uitrekent.

#### Voorbeeld
Een windsterkte van $$4.3 \dfrac{\text{km}}{\text{u}}$$ leidt tot:
```
1 Beaufort
```

Een windsterkte van $$108 \dfrac{\text{km}}{\text{u}}$$ leidt tot:
```
11 Beaufort
```

{: .callout.callout-info}
> #### Tips
> - Vergeet niet om te rekenen van km / u naar m / s.
> - Gebruik de functie `int()` om een kommagetal `11.0` als `11` te schrijven.