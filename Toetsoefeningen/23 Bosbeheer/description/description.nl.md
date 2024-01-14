Goed bosbeheer is van veel belang om een bos in stand te houden. Daar hoort ondere bij dat zieke bomen geveld worden en er nieuwe bomen worden aangeplant.

![Foto door Ruben Hanssen op Unsplash.](media/ruben-hanssen.jpg "Foto door Ruben Hanssen op Unsplash."){:data-caption="Foto door Ruben Hanssen op Unsplash." width="45%"}


## Opgave

Schrijf een programma dat de gebruiker vraagt naar het aantal bomen in een bos. Daarna vraag je de gebruiker in volgorde **hoeveel procent** er jaarlijks gekapt wordt en **hoeveel nieuwe bomen** er jaarlijks bijgeplant worden.

Bereken vervolgens hoe het aantal bomen evolueert na 100 jaar, waarbij je elke 10 jaar het aantal bomen weergeeft.

#### Voorbeeld
Indien er `2000` bomen zijn en er wordt jaarlijks `5` procent gekapt en nadien `120` bomen bijgeplant, dan verschijnt er:

```
Er zijn eerst 2000 bomen.
na 10 jaar zijn er 2165 bomen.
na 20 jaar zijn er 2263 bomen.
na 30 jaar zijn er 2322 bomen.
na 40 jaar zijn er 2357 bomen.
na 50 jaar zijn er 2378 bomen.
na 60 jaar zijn er 2389 bomen.
na 70 jaar zijn er 2399 bomen.
na 80 jaar zijn er 2400 bomen.
na 90 jaar zijn er 2400 bomen.
na 100 jaar zijn er 2400 bomen.
```

5% van 2000 is 100 en daarna worden er 120 bijgeplant. Dit levert na 1 jaar dus 2020 bomen op. Het proces herhalen leidt na 2 jaar tot 2039 bomen. Hiervan 5% berekenen levert 101,95, of met andere woorden 101 bomen (naar beneden afgerond). Zodat er na 3 jaar 2058 bomen zijn, enz...

{: .callout.callout-info}
> #### Tips
> - Vraag het aantal percentage als een geheel getal. Bij 5% tikt de gebruiker 5 in.
> - Bereken telkens eerst hoeveel bomen er omgehakt worden. Rond hierbij af naar beneden met behulp van `math.floor()`.

