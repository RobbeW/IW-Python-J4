Windkracht wordt uitgedrukt in de <a href="https://nl.wikipedia.org/wiki/Schaal_van_Beaufort" target="_blank">schaal van Beaufort</a>. Oorspronkelijk telde de schaal 13 waarden, maar sinds 1946  werd een nieuwe schaal ontwikkeld die 17 waarden telt. Men berekent de Beaufort windsnelheid $$B$$ via de volgende formule:

$$
    B = \left(\dfrac{v}{0,836}\right)^\dfrac{2}{3}
$$

Hierbij wordt de Beaufort windsnelheid steeds afgerond op **eenheden** nauwkeurig. 

![Een windsok op het Nederlands strand.](media/beaufort.jpg "Foto door RoonZ nl op Unsplash."){:data-caption="Een windsok op het Nederlands strand." width="40%"}

## Opgave
Schrijf een programma dat de windsnelheid $$v$$ in $$\dfrac{\text{m}}{\text{s}}$$ vraagt en vervolgens de Beaufort windsnelheid uitrekent.

#### Voorbeeld
Een windsterkte van $$1.2 \dfrac{\text{m}}{\text{s}}$$ leidt tot:
```
1 Beaufort
```

Een windsterkte van $$30 \dfrac{\text{m}}{\text{s}}$$ leidt tot:
```
11 Beaufort
```

{: .callout.callout-info}
> #### Tip
> Gebruik de functie `int()` om een kommagetal `11.0` als `11` te schrijven.