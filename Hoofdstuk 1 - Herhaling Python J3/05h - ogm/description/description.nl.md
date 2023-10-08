## Opgave
Vaak wordt aan een overschrijving een gestructureerde mededeling (ogm) toegevoegd. Met behulp van deze mededeling kan de ontvangende partij gemakkelijk controleren of het correcte bedrag werd overgeschreven. De mededeling vind je onderaan een overschrijvingsformulier:

![ogm](media/ogm.jpg "ogm"){:data-caption="Een overschrijvingsformulier met onderaan de gestructureerde mededeling" width="45%"}

Deze mededeling bestaat steeds uit **drie getallen** van achtereenvolgens 3, 4 en 5 cijfers.

$$
\mathsf{016/1780/000\,\,\mathbf{05}}
$$

Er is een mechanisme in deze mededeling ingebouwd, zodat je beschermd bent tegen tikfoutjes. De laatste 2 cijfers (het controlegetal) zijn immers steeds de rest bij deling van alle voorgaande getallen door 97. In het bovenstaande geval zal je merken dat 161 780 000 rest 5 heeft bij een deling door 97.

Indien de rest nul bedraagt wordt het getal 97 als controlegetal gebruikt.

Maak nu een programma dat achtereenvolgens een getal van 3, 4 en tot slot opnieuw 3 cijfers vraagt en vervolgens de gestructureerde medeling op het scherm weergeeft.

#### Voorbeeld
Voor het bovenstaande voorbeeld zouden de getallen `016`, `1780` en `000` dus leiden tot:
```
+++016/1780/00005+++
```

{: .callout.callout-info}
> #### Tip
> Je kan voorloopnullen creëren via `zfill()`, bijvoorbeeld: `str( getal2 ).zfill(4)`. Dit zorgt ervoor dat `getal4` steeds geschreven wordt met voorloopnullen tot er vier tekens zijn.

