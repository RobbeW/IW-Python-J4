Bij koud weer met een gure wind zal je de koude veel meer aanvoelen dan indien het windstil is. De temperatuur die je aanvoelt, de gevoelstemperatuur, ligt dan lager dan de echte temperatuur. Er zijn verschillende methodes om de gevoelstemperatuur te bepalen. Eén van die methoden is de JAG/TI-methode (*Joint Action Group on Weather Indices*). 

![Afbeelding door Ben White op Unsplash.](media/ben-white.jpg "Afbeelding door Ben White op Unsplash."){:data-caption="Afbeelding door Ben White op Unsplash."  width="45%"}

Deze in Canada ontwikkelde methode resulteerde in onderstaande formule:

$$
\mathsf{G = 13,12 + 0,6215\cdot T  + (0,3965\cdot T - 11,37)\cdot (3,6 \cdot W)^{0,16}}
$$

Hierbij stelt T de luchtemperatuur in °C en W de windsnelheid in km/u voor.

## Opgave

Programmeer de functie `gevoelstemperatuur(T, W)` die gegeven de luchttemperatuur `T` en de windsnelheid `W` de gevoelstemperatuur retourneert. Rond hierbij af op 2 decimalen.

Vraag daarna in volgorde naar de luchttemperatuur en de windsnelheid en gebruik de functie `gevoelstemperatuur(T, W)` om de gevoelstemperatuur weer te geven.

#### Voorbeeld
Bij een temperatuur van `10.0` °C en een windsnelheid van `5.0` km/u verschijnt er:

```
De temperatuur voelt aan als 9.76 °C.
```

Want de uitvoer van de functie is als volgt:
```python
>>> gevoelstemperatuur(10.0, 5.0)
9.76
```
