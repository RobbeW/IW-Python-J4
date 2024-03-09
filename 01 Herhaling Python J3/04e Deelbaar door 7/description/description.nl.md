Er bestaat een methode om manueel te controleren of een getal deelbaar is door 7. De methode werkt als volgt:

- Verdubbel het cijfer van de eenheden;
- Bereken het verschil van het getal zonder het cijfer van de eenheden en het vorig getal;
- Is dit verschil duidelijk deelbaar door 7, dan ben je klaar. Zo niet, herhaal.

![Het getal 7.](media/alejandro-barba.jpg "Foto door Alejandro Barba op Unsplash."){:data-caption="Het getal 7." width="25%"}

Beschouw bijvoorbeeld het getal 3024. Het cijfer van de eenheden is 4, het dubbele hiervan is 8. Het getal zonder het cijfer van de eenheden is 302. Het verschil van 302 en 8 is 294.

Het proces wordt nogmaals herhaald, maar nu met de uitkomst van het vorige getal, namelijk 294. Het cijfer van de eenheden is opnieuw 4, het dubbele is 8. Het getal zonder het cijfer van de eenheden is 29. Het verschil van 29 en 8 is 21. 

Omdat 21 nu duidelijk deelbaar is door 7 geldt er dat het volledig getal, 3024 ook deelbaar is door 7.

## Gevraagd
Schrijf een progamma dat een getal vraagt aan de gebruiker en dit proces uitvoert. Net zoals in het voorbeeld moet dit proces twee keer uitgevoerd worden.

#### Voorbeeld 1
De invoer `3024` levert als uitvoer
```
1e stap: Het verschil van 302 en 8 is 294
2e stap: Het verschil van 29 en 8 is 21
21 is duidelijk deelbaar door 7, dus ook 3024 is deelbaar door 7.
```

#### Voorbeeld 2
De invoer `4711` levert als uitvoer
```
1e stap: Het verschil van 471 en 2 is 469
2e stap: Het verschil van 46 en 18 is 28
28 is duidelijk deelbaar door 7, dus ook 4711 is deelbaar door 7.
```
