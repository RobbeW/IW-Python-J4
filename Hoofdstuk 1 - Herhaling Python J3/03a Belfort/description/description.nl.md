Wim wil de hoogte van een Belfort meten. Daarvoor gebruikt hij een laser van een bouwbedrijf. 
Met deze laser kan je eenvoudig een straal fotonen schieten naar een punt. Wanneer deze terugkaatsen, dan vertelt het toestel de afstand tussen Wim en het object. 

![Het belfort in Gent.](media/juli-sure.jpg "Foto door Juli Sure op Pexels."){:data-caption="Het belfort in Gent." width="30%"}

## Opgave

Wim mikt de laser op de basis (waar de toren en de grond elkaar raken) en de top van de toren. 

Schrijf een programma dat de corresponderende afstanden in deze volgorde aan de gebruiker **vraagt** en vervolgens de **hoogte** van de toren tot op **3 cijfers na de komma** berekent en op het scherm **afdrukt**.

#### Voorbeelden

Bij het <a href="https://nl.wikipedia.org/wiki/Belfort_van_Gent" target="_blank">belfort van Gent</a> meet Wim als afstand tot de basis `48.789` en als afstand tot de top `107.437`. Het programma geeft vervolgens het volgende weer:

```
Dit belfort is 95.72 m hoog.
```

Bij het <a href="https://nl.wikipedia.org/wiki/Belfort_van_Aalst" target="_blank">belfort van Aalst</a> meet Wim als afstand tot de basis `39.924` en als afstand tot de top `61.354`. Het programma geeft vervolgens het volgende weer:

```
Dit belfort is 46.587 m hoog.
```

{: .callout.callout-info}
> #### Tips
> - Je zal de stelling van Pythagoras nodig hebben.
> - Vierkantswortels berekenen doe je via `import math` en de functie `math.sqrt()`.