## Gegeven
Zoals wel vaker in de wiskunde gebeurt, werd de Leibniz-formule niet naar de eerste persoon die deze ontdekte vernoemd. In de 14e eeuw was Madhava of Sangamagrama de eerste die deze reeks vond, maar werd pas een kleine 300 jaar later door Gottfried Leibniz herontdekt en gedocumenteerd.

![Erik in de wiskundeles.](media/wiskunde_les.jpg "Erik in de wiskundeles."){:data-caption="Erik in de wiskundeles." width="45%"}

Beide wiskundigen ontdekten dat volgende reeks gelijk is aan $$\frac{\pi}{4}$$:

$$
\mathsf{\dfrac{\pi}{4} = \dfrac{1}{1} - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \dfrac{1}{9} - \dfrac{1}{11} + \ldots}
$$

Je kan deze uitdrukking omvormen om de waarde van π te berekenen (in de praktijk: *benaderen*)

$$
\mathsf{\pi = 4 \cdot \left( \dfrac{1}{1} - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \dfrac{1}{9} - \dfrac{1}{11} + \ldots \right)}
$$

## Opgave
Bepaal een benadering voor het getal π met bovenstaande uitdrukking. Schrijf een programma dat naar het aantal termen vraagt en vervolgens via een begrensde herhaling de benadering uitrekent. Rond de benadering af op **6 cijfers na de komma**.


#### Voorbeelden

Indien de gebruiker `2` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{4 \cdot \left(\dfrac{1}{1} - \dfrac{1}{3}\right ) \approx 2,666666\ldots}
$$

Zodat er verschijnt:
```
De Leibniz-benadering van pi met 2 termen is 2.666667
```


Indien de gebruiker `10` intikt, dan wordt de volgende berekening uitgevoerd:

$$
\mathsf{4 \cdot \left(\dfrac{1}{1} - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \dfrac{1}{9} - \dfrac{1}{11} + \dfrac{1}{13} - \dfrac{1}{15} + \dfrac{1}{17} - \dfrac{1}{19}\right) \approx 3,041839\ldots}
$$

Zodat er verschijnt:
```
De Leibniz-benadering van pi met 10 termen is 3.04184
```