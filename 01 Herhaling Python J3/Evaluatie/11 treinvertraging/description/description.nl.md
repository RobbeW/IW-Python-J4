De stiptheid van de treinen op het Belgische spoornet vormt soms een probleem. Volgens dit <a href="https://www.vrt.be/vrtnws/nl/2023/03/08/stiptheid-treinen-februari/" target="_blank">artikel</a> reed in februari 2023 meer dan één op de zes treinen met een vertraging.

![Een typische dag met vertragingen bij de NMBS.](media/treinvertraging.jpg "Een typische dag met vertragingen bij de NMBS."){:data-caption="Een typische dag met vertragingen bij de NMBS." width="40%"}

## Opgave
Schrijf een programma dat eerst het tijdstip van vertrek vraagt aan de gebruiker. Eerst het **uur van vertrek**, daarna de **minuten van vertrek**.
Vervolgens vraagt het programma naar de reistijd, door **opnieuw** eerst de uren en de minuten op te vragen. Tot slot vraagt je programma naar het **aantal minuten** vertraging.

Bereken daarna wanneer de trein op de bestemming zal toekomen.

#### Voorbeeld
Voor een trein met vertrektijd `14`.`25` u. en `2` uur en `20` minuten reistijd met `30` minuten vertraging verschijnt er:

```
Je trein komt aan om 17.15 u.
```

{: .callout.callout-info}
> #### Tips
> - Je zal in deze oefening **vijf keer** een getal moeten vragen aan de gebruiker.
> - Om het punt `.` tussen de uren en de minuten aan de uren vast te *plakken* kan je gebruik maken van `str()` (om een getal om te zetten naar tekst) en `+` (om te concateneren - tekst samenvoegen - zonder spatie).