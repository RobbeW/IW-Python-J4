Baby Charlie wordt één jaar en leert net hoe hij kan tellen. Zijn favoriete bezigheid is tellen hoeveel happen hij neemt tijdens een maaltijd. Telkens hij een hap neemt, telt hij het getal.

![Foto door Christopher Luther op Unsplash.](media/christopher-luther.jpg "Foto door Christopher Luther op Unsplash."){:data-caption="Foto door Christopher Luther op Unsplash." width="45%"}

Maar tellen met een volle mond lukt natuurlijk niet altijd, soms mompelt hij maar wat. Je vermoedt dat hij de tel vaak verliest.

## Opgave

Maak een programma dat controleert of Charlie al dan niet de tel heeft verloren. Als eerste vraagt je programma naar het aantal happen dat Charlie nam. Vervolgens geef je evenveel keer een getal of de tekst `"gemompel"` in. Nadien verschijnt er: `"Dit lijkt te kloppen."` of `"Hier klopt iets niet..."`

#### Voorbeeld

Bij invoer `5` en daarna de achtereenvolgende invoer `1`, `2`, `3`, `gemompel`, `5` verschijnt:

```
Dit lijkt te kloppen.
```

Bij invoer `8` en daarna de achtereenvolgende invoer `1`, `2`, `3`, `gemompel`, `gemompel`, `7`, `gemompel`, `8` verschijnt:

```
Hier klopt iets niet...
```

Bij invoer `3` en daarna de achtereenvolgende invoer `gemompel`, `gemompel`, `gemompel` verschijnt:

```
Dit lijkt te kloppen.
```

{: .callout.callout-info}
>#### Tip
> Gebruik `int()` om tekst naar een geheel getal om te zetten.

{: .callout.callout-secondary}
>#### Bron
> Nordic Collegiate Programming Contest (NCPC) 2018