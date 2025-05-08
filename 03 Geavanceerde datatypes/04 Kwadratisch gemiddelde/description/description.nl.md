Het kwadratisch gemiddelde van $$\mathsf{n}$$ getallen $$\mathsf{x_1}$$, $$\mathsf{x_2}$$, ..., $$\mathsf{x_n}$$ wordt als volgt berekend:

$$
\mathsf{\sqrt{\dfrac{1}{n} \cdot (x_1^2+ x_2^2 + \ldots + x_n^2)}}
$$

Dit gemiddelde wordt zeer frequent gebruikt binnen de verklarende statistiek.

## Opgave

Programmeer een functie `kwadratisch_gemiddelde(lijst)`, zodat deze gegeven een lijst met getallen het kwadratisch gemiddelde uitrekent. Rond dit gemiddelde af op 3 decimalen.

#### Voorbeeld

```python
>>> kwadratisch_gemiddelde([-17.7, -23.5, -28.2, -22.5, -17.1])
22.179
```

{: .callout.callout-info}
> #### Tip
> Vergeet de `math` module niet te importeren.
