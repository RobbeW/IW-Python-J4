In 1741 lostte <a href='https://nl.wikipedia.org/wiki/Leonhard_Euler' target='_blanc'>Euler</a> het beroemde <a href='https://nl.wikipedia.org/wiki/Bazel-probleem' target='_blanc'>Bazel-probleem</a> op. 

Hij bewees dat de (oneindige) som van de omgekeerden van de kwadraten van de natuurlijke getallen gelijk is aan $$\frac{\pi^2}{6}$$, met andere woorden:

$$
\mathsf{\dfrac{\pi^2}{6} = \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots}
$$

Je kan deze uitdrukking omvormen om de waarde van π te berekenen (in de praktijk: *benaderen*)

$$
\mathsf{\pi = \sqrt{6\cdot \left( \dfrac{1}{1^2}+\dfrac{1}{2^2}+\dfrac{1}{3^2}+\dfrac{1}{4^2}+\ldots \right)}}
$$

## Opgave

Bepaal een benadering voor het getal π met bovenstaande uitdrukking. Schrijf een programma dat naar het aantal termen vraagt en vervolgens via een **voorwaardelijke herhaling** de benadering uitrekent. Rond de benadering af op **6 cijfers na de komma**.

#### Voorbeelden
Indien de gebruiker `2` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{\sqrt{6 \cdot \left(\dfrac{1}{1^2} + \dfrac{1}{2^2}\right ) } \approx 2,738613\ldots}
$$

Zodat er verschijnt:
```
De Bazel-benadering van pi met 2 termen is 2.738613
```


Indien de gebruiker `4` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{\sqrt{6 \cdot \left(\dfrac{1}{1^2} + \dfrac{1}{2^2}+ \dfrac{1}{3^2}+\dfrac{1}{4^2}\right )}\approx 2,922613\ldots}
$$

Zodat er verschijnt:
```
De Bazel-benadering van pi met 4 termen is 2.922613
```
