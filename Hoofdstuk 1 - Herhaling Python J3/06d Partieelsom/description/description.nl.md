Onderstaande **oneindige** som noemt men in de wiskunde een **reeks**.

$$
\mathsf{\dfrac{1}{2} + \dfrac{1}{4} +\dfrac{1}{8}+\dfrac{1}{16}+\dfrac{1}{32}+\ldots}
$$

Het valt vrij eenvoudig te bewijzen dat deze **oneindige** som uitrekenen in het getal 1 resulteert. Hieronder zie je een *meetkundig bewijs*, de volledige reeks vult namelijk een vierkant met oppervlakte 1.

![Een wiskundige reeks.](media/image.png "Een wiskundige reeks."){:data-caption="Een wiskundige reeks." .light-only width="20%"}

![Een wiskundige reeks.](media/image_dark.png "De som van Archimedes"){:data-caption="Een wiskundige reeks." .dark-only width="20%"}

Een **oneindige** som kan je in realiteit niet uitvoeren, maar je kan deze wel benaderen via een **partieelsom**. Zo is de partieelsom van de eerste 2 termen gelijk aan:

$$
\mathsf{\dfrac{1}{2} + \dfrac{1}{4} = 0,75}
$$

En de partieelsom van de eerste 4 termen:

$$
\mathsf{\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8}+ \dfrac{1}{16} = 0,9375}
$$

## Opgave
Schrijf een programma dat naar het aantal termen vraagt en vervolgens via een begrensde herhaling de partieelsom uitrekent die hiermee overeenkomt.
Rond de partieelsom af op **6 cijfers na de komma**.

#### Voorbeelden
Geef de gebruiker `2` in, dan verschijnt er:
```
De som van de eerste 2 termen is 0.75
```

Geef de gebruiker `4` in, dan verschijnt er:
```
De som van de eerste 4 termen is 0.9375
```
