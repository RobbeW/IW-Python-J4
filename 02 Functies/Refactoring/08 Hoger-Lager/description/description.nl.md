## Opgave

Schrijf een programma dat een willekeurig getal neemt tussen 1 en 1 000. Het programma vraagt de gebruiker het getal te raden. Na iedere gok van de gebruiker komt een boodschap:

- "Het getal is lager dan ..." indien je lager moet gokken,
- "Het getal is hoger dan ..." indien je hoger moet gokken,
- "Je hebt ... geraden in ... pogingen!" indien de gok correct is.

Schrijf een functie `hogerLager(getal)` dat een willekeurig getal vraagt, deze outputs geeft en uiteindelijk het aantal pogingen returnt.

#### Voorbeeld

Stel dat het willekeurige getal `614` is, indien de gebruiker achtereenvolgens de getallen `500`, `750`, `600` en `614` ingeeft, dan verschijnt er:

```
Het getal is hoger dan 500
Het getal is lager dan 750
Het getal is hoger dan 600
Je hebt 614 geraden in 4 pogingen!
```

{: .callout.callout-info}
> #### Tips
> - Gebruik `random.randint(1, 1000)` om een willekeurig getal tussen 1 en 1 000 door de computer te laten genereren.
> - Geef het *te raden getal* weer terwijl je het programma uittest.
