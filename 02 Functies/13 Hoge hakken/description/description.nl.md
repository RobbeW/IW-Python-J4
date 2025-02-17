Britse wetenschappers hebben onderzocht hoe groot de maximale hakhoogte van schoenen voor meisjes en vrouwen mag zijn. Zij adviseren een meisje dat voor het eerst op hoge hakken wil gaan lopen, een hakhoogte h (in cm) volgens onderstaande formule te kiezen:

$$
    \mathsf{h = \dfrac{1}{2} \cdot (12 + 0,375 \cdot s )}
$$

waarbij s de Britse schoenmaat voorstelt.

![Afbeelding door Kris Atomic op Unsplash.](media/kris-atomic.jpg "Afbeelding door Kris Atomic op Unsplash."){:data-caption="Afbeelding door Kris Atomic op Unsplash."  width="45%"}

Indien men rekening wil houden met het aantal uur dat de hakken gedragen zullen worden, dan wordt de formule wat aangepast. Men maakt dan gebruik van de wankelfactor W:

$$
    \mathsf{h = W \cdot (12 + 0,375 \cdot s ) \qquad \text{met}\qquad W = \dfrac{28}{45 \cdot (0,5 \cdot A +1)}} 
$$

waarbij A het aantal uur is dat een vrouw achter elkaar op hoge hakken loopt of staat.

## Opgave

* Programmeer de functie `wankelfactor(aantal_uur)` die de wankelfactor retourneert, **afgerond** op twee decimalen.

* Programmeer daarna de functie `hakhoogte(s, w)` die de hakhoogte retourneert, **afgerond** op één decimaal. In deze functie is de parameter `w` een **optionele parameter**. Met andere woorden `hakhoogte(6.0)` berekent de hakhoogte met de eerste formule, terwijl `hakhoogte(6.0, 0.3)` de tweede formule gebruikt. 

* Vraag **hierna** aan de gebruiker de (Britse) schoenmaat en of de gebruiker rekening wil houden met het aantal uren dat deze recht zal staan. Indien de gebruiker daarop `"J"` antwoordt, dan vraag je naar dat aantal uur. Geef uiteindelijk de maximale hakgrootte weer. Gebruik de functies.

#### Voorbeeld 1

Indien een gebruiker `10.5` als schoenmaat intikt en `"N"` antwoordt op de vraag:
```
Je kan hakken tot 8.0 cm dragen.
```

want de achterliggende functie werd als volgt gebruikt:
```python
>>> hakhoogte(10.5)
8.0
```

#### Voorbeeld 2
Indien de gebruiker `10.5` als schoenmaat intikt en  `"J"` gevolgd door `4` intikt, dan verschijnt er:

```
Je mag hakken tot 3.3 cm dragen.
```

want de achterliggende functies werden als volgt gebruikt:
```python
>>> wankelfactor(4)
0.21
```

```python
>>> hakhoogte(10.5, 0.21)
3.3
```

