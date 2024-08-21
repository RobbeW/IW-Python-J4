Naast het gewone, **rekenkundige**, gemiddelde zijn er ook andere manieren om een gemiddelde van getallen te berekenen. Eén van deze methodes is het zogenaamde *harmonisch* gemiddelde. Het **harmonisch gemiddelde** x<sub>h</sub> van de reële getallen a en b is gedefinieerd als:

$$
    \mathsf{x_h = \dfrac{2}{\frac{1}{a}+\frac{1}{b}}}
$$

## Opgave

Schrijf een functie `harmonisch_gemiddelde(a, b)` die het harmonisch gemiddelde berekent, rond hierbij af op 2 cijfers.

Vraag aan de gebruiker **vervolgens** twee getallen `a` en `b` en laat de functie `harmonisch_gemiddelde` het harmonisch gemiddelde ervan berekenen. Druk dit harmonisch gemiddelde vervolgens af op het scherm.

#### Voorbeelden
Indien de gebruiker `100` en `120` intikt, dan verschijnt er:
```
Het harmonisch gemiddelde van 100 en 120 is 109.09
```
want er geldt:
```python
>>> harmonisch_gemiddelde(100, 200)
109.09
```

Indien de gebruiker `128` en `26` intikt, dan verschijnt er:
```
Het harmonisch gemiddelde van 128 en 26 is 43.22
```
want er geldt:

```python
>>> harmonisch_gemiddelde(100, 200)
43.22
```