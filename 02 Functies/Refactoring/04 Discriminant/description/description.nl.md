De <a href='https://nl.wikipedia.org/wiki/Discriminant' target='_blanc'>discriminant</a> is de uitdrukking die zal bepalen of een vierkantsvergelijking al dan niet oplossingen heeft.

## Opgave

Schrijf een programma dat van een **vierkantsvergelijking** (in de algemene vorm) $$\mathsf{ax^2+bx+c=0}$$ achtereenvolgens de waarden van de coëfficienten $$\mathsf{a}$$, $$\mathsf{b}$$ en $$\mathsf{c}$$ vraagt. 

De discriminant wordt vervolgens op een specifieke manier weergegeven (rond af op één cijfer). Erna wordt weergeven of er geen, één of twee verschillende reële oplossingen zijn.

Maak gebruik van de functies `discriminant(...)` en `printOplossing(...)` om respectievelijk de discriminant te berekenen en alle tekst naar het scherm te printen.

#### Voorbeelden
De vierkantsvergelijking $$\mathsf{2x^2+6x+5 = 0}$$ heeft als discriminant -4.
```
Discriminant = -4.0
Er zijn geen reële oplossingen.
```

De vierkantsvergelijking $$\mathsf{x^2+2x+1 = 0}$$ heeft als discriminant 0.
```
Discriminant = 0.0
Er is exact één reële oplossing.
```

De vierkantsvergelijking $$\mathsf{x^2+3x-4 = 0}$$ heeft als discriminant 25.
```
Discriminant = 25.0
Er zijn twee verschillende reële oplossingen.
```



