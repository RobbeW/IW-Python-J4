Goed bosbeheer is van veel belang om een bos in stand te houden. Daar hoort ondere bij dat zieke bomen geveld worden en er nieuwe bomen worden aangeplant.

![Foto door Ruben Hanssen op Unsplash.](media/ruben-hanssen.jpg "Foto door Ruben Hanssen op Unsplash."){:data-caption="Foto door Ruben Hanssen op Unsplash." width="45%"}

Een voorbeeld van goed bosbeheer is om jaarlijks een bepaald percentage om te hakken en daarnaast een aantal nieuwe bomen te planten. Zo kan men bijvoorbeeld jaarlijks 5% van de bomen kappen en er jaarlijks ook 120 bijplanten. Indien men dit doet dan evolueert het aantal bomen in het bos naar een **evenwicht**, een **equilibrium**.

Dit is een voorbeeld van een zogenaamd **dynamisch discreet proces**.

## Opgave

Schrijf een programma dat de gebruiker vraagt naar het aantal bomen in een bos. Daarna vraag je de gebruiker in volgorde **hoeveel procent** er jaarlijks gekapt wordt en **hoeveel nieuwe bomen** er jaarlijks bijgeplant worden.

Bereken vervolgens op welk aantal bomen bovenstaand proces stabiliseert.

#### Voorbeeld
Indien er `200` bomen zijn en er wordt jaarlijks `5` procent gekapt en nadien `15` bomen bijgeplant, dan verschijnt er:

```
Er zijn eerst 200 bomen in het bos.
na 1 jaar zijn er 205 bomen.
na 2 jaar zijn er 210 bomen.
na 3 jaar zijn er 215 bomen.
na 4 jaar zijn er 220 bomen.
na 5 jaar zijn er 224 bomen.
...
na 40 jaar zijn er 295 bomen.
na 41 jaar zijn er 296 bomen.
na 42 jaar zijn er 297 bomen.
na 43 jaar zijn er 298 bomen.
na 44 jaar zijn er 299 bomen.
na 45 jaar zijn er 300 bomen.
na 46 jaar zijn er 300 bomen.
Er zullen uiteindelijk 300 bomen in het bos zijn.
```

{: .callout.callout-info}
> #### Tips
> - Vraag het aantal percentage als een geheel getal. Bij 5% tikt de gebruiker 5 in.
> - Bereken telkens eerst hoeveel bomen er omgehakt worden. Rond hierbij af naar beneden met behulp van `math.floor()`.

