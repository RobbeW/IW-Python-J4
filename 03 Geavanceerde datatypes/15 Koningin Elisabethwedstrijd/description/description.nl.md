De <a href="https://nl.wikipedia.org/wiki/Koningin_Elisabethwedstrijd" target="_blank">Koningin Elisabethwedstrijd<a/> is een bekende driejaarlijkse muziekwedstrijd opgericht in 1937 door Koningin Elisabeth van België. Afwisselend treden pianisten, violisten en zangers voor een professionele vakjury.

Het volledige quoteringssysteem is vrij ingewikkeld, zoals beschreven in <a href="https://www.vrt.be/vrtnws/nl/2024/05/14/koningin-elisabethwedstrijd-hoe-beslist-de-jury/" target="_blank">dit artikel</a> van 16 mei 2024 door VRT NWS.

Er zit een regel in het quoteringssysteem ingebakken dat verhindert dat één jurylid een kandidaat ophemelt of in de grond boort. Indien een jurylid namelijk **meer dan 20% afwijkt** van het gemiddelde van de andere juryleden, dan wordt de score aangepast tot het verschil hoogstens 20% bedraagt.
Op het einde neemt men het gemiddelde van alle (mogelijks aangepaste) scores.

Een voorbeeld zal heel wat verduidelijken. Stel dat de scores van de jury de volgende zijn: `[63, 90, 55, 67, 59, 56]`. Je merkt meteen dat het tweede jurylid nogal gul was in de beoordeling. En inderdaad, indien je het gemiddelde van de andere scores berekent bekom je 60. De score van het tweede jurylid is dus zo maar even 50% meer dan het gemiddelde van de rest. De score van dit jurylid wordt dus aangepast tot 72, 72 is namelijk 20% meer dan 60.

## Opgave

Programmeer een functie `elisabeth_wedstrijd(punten)` dat gegeven een lijst met punten (telkens op 100), de uiteindelijke score uitrekent. Rond in je eindberekening af tot op 2 cijfers.

#### Voorbeeld

```
>>> elisabeth_wedstrijd([63, 90, 55, 67, 59, 56])
62.0
```


{: .callout.callout-info}
>#### Tip
> Bij de vergelijking met het gemiddelde van de andere juryleden kijk je steeds terug naar de oorspronkelijke punten. Je zal dus een nieuwe lijst `punten_nieuw` moeten aanmaken waar je ofwel het oorspronkelijke punt (indien niet teveel afwijkend) ofwel het aangepaste punt aan toevoegt. Uiteindelijk bepaal je dan het gemiddelde van deze nieuwe lijst.