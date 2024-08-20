Baby Jutta wordt één jaar en leert net hoe ze kan tellen. Haar favoriete bezigheid is tellen hoeveel happen ze neemt tijdens een maaltijd. Telkens ze een hap neemt, telt ze het getal.

![Foto door Christopher Luther op Unsplash.](media/christopher-luther.jpg "Foto door Christopher Luther op Unsplash."){:data-caption="Foto door Christopher Luther op Unsplash." width="45%"}

Maar tellen met een volle mond lukt natuurlijk niet altijd, soms mompelt ze maar wat. Soms vermoed je dat ze de tel verliest.

## Opgave

Maak een programma dat controleert of Jutta al dan niet de tel heeft verloren. Als eerste vraagt je programma naar het aantal happen dat Jutta nam. Vervolgens geef je evenveel keer een getal of de tekst "gemompel" in. Nadien verschijnt er: `"Dit lijkt te kloppen."` of `"Hier klopt iets niet..."`

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