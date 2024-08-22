De <a href="https://nl.wikipedia.org/wiki/Vlag_van_de_Verenigde_Staten" target="_blank">Stars and Stripes</a> is de bijnaam van de gekende vlag van de Verenigde Staten van Amerika. Deze bestaat uit 7 rode horizontale strepen gescheiden door 6 witte strepen. In het linkerbovenhoek vinden we 50 witte sterren op een blauwe achtergrond. Deze sterren stellen de 50 staten van de Verenigde Staten voor.

![Foto door R. D. Smith op Unsplash.](media/R_D_Smith.jpg "Foto door R. D. Smith op Unsplash."){:data-caption="Foto door R. D. Smith op Unsplash." width="45%"}

Het huidige patroon van deze sterren is als volgt, vijf rijen met telkens 6 sterren en ertussen vier rijen met telkens 5 sterren, samen 50 sterren.

```
1:  * * * * * *
A:   * * * * *
2:  * * * * * *
B:   * * * * *
3:  * * * * * *
C:   * * * * *
4:  * * * * * *
D:   * * * * *
5:  * * * * * *
```

Dit patroon noemt men ook wel het **6 ; 5 patroon**. De eerste rij bevat immers 6 sterren, de volgende rij bevat er 5.

Stel dat <a href="https://nl.wikipedia.org/wiki/Puerto_Rico" target="_blank">Puerto Rico</a> lid wordt van de Verenigde Staten van Amerika, hoe kan men deze vlag dan aanpassen zodat het aantal sterren 51 is? Een mogelijkheid is dan het **9 ; 8 patroon**. Dit betekent dat er dan drie rijen van 9 sterren zijn en drie rijen van 8 sterren, telkens afwisselend.

Indien een staat de Verenigde Staten van Amerika zou verlaten resteren 49 sterren en zou men een **7 ; 7 patroon** kunnen gebruiken.


We noemen een vlag visueel geslaagd indien deze voldoet aan de volgende criteria:

- Elke opeenvolgende rij mag niet meer dan één ster verschillen van de vorige;
- Elke andere rij heeft eenzelfde aantal sterren;
- De eerste rij mag niet minder sterren hebben dan de tweede rij.

## Opgave

Ontwerp een algoritme dat gegeven een aantal sterren groter dan 3 alle mogelijke patronen geeft die aan de criteria voldoen. De patronen moeten afgedrukt worden volgens een stijgend aantal sterren op de eerste rij.

##### Voorbeelden

Bij invoer `3` verschijnt:
```
2 ; 1
```

Bij invoer `50` verschijnt:
```
2 ; 1
2 ; 2
3 ; 2
5 ; 4
5 ; 5
6 ; 5
10 ; 10
13 ; 12
17 ; 16
25 ; 25
```

Bij invoer `51` verschijnt:
```
2 ; 1
3 ; 3
9 ; 8
17 ; 17
26 ; 25
```

{: .callout.callout-secondary}
>#### Bron
> ICPC Mid-Atlantic Regional Contest 2017