De schaal van Beaufort werd in 1805 opgesteld door de Ier <a href="https://nl.wikipedia.org/wiki/Francis_Beaufort" target="_blank">Francis Beaufort</a>. Het is een manier om de snelheid van de wind te classificeren.

![Afbeelding door Nathan Anderson op Unsplash.](media/nathan-anderson.jpg "Afbeelding door Nathan Anderson op Unsplash."){:data-caption="Afbeelding door Nathan Anderson op Unsplash."  width="40%"}

Indien men de windkracht uitgedrukt in een aantal Beaufort (B) kent, dan kan men de windsnelheid (v) in m/s *benaderen* via de formule:

$$
\mathsf{v \approx 0,8360 \cdot B^{\frac{3}{2}}}
$$

## Opgave

Kopieer het programma uit de vorige oefening, je zal aan dat programma enkele functies **toevoegen**.

* Programmeer een functie `beaufort_naar_km_u(B)` die gegeven de Beaufort schaal de benaderende windsnelheid in **km/u** retourneert. Je rondt dit af op **6 decimalen**.

* Programmeer een functie `gevoelstemperatuur_beaufort(T, B)` die gegeven de luchttemperatuur `T` en de windsnelheid uitgedrukt in de schaal van Beaufort de gevoelstemperatuur retourneert. In deze functie gebruik je zowel de functie `beaufort_naar_km_u(B)` als de functie `gevoelstemperatuur(T, W)`.

* Vraag daarna **in volgorde** naar de luchttemperatuur en de windsnelheid **en de eenheid van windsnelheid**. Indien de gebruiker `"B"` intikt gebruik je de laatste functie. Indien de gebruiker `"km/u"` intikt gebruik je de functie `gevoelstemperatuur(T, W)` om de gevoelstemperatuur te berekenen. Geef deze nadien ook weer.

#### Voorbeeld 1

Bij een temperatuur van `10.0` °C en een windsnelheid van `5.0` `"km/u"` verschijnt er:

```
De temperatuur voelt aan als 7.58 °C.
```

Want de uitvoer van de functie is als volgt:
```python
>>> gevoelstemperatuur(10.0, 5.0)
7.58
```

#### Voorbeeld 2

Bij een temperatuur van `3.0` °C en een windsnelheid van `5` `"B"` verschijnt er:

```
De temperatuur voelt aan als -6.95 °C.
```

Want de uitvoer van de bijbehorende functies is als volgt:
```python
>>> gevoelstemperatuur_beaufort(3.0, 5)
-6.95
```
die gebruikt maakt van: 
```python
>>> beaufort_naar_km_u(5)
33.648351
```
