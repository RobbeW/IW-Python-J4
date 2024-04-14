Een CAS-nummer is een unieke numerieke identificatie voor chemische elementen. CAS staat voor *Chemical Abstracts Service*.

Via <a href="https://commonchemistry.cas.org/" target="_blank">deze website</a> kan je bijvoorbeeld gemakklijk CAS-nummers gaan opzoeken.

Er geldt bijvoorbeeld dat <a href="https://commonchemistry.cas.org/detail?cas_rn=58-08-2" target="_blank">58-08-2</a> het CAS-nummer van cafeïne is. Het nummer wordt op een bepaalde manier opgebouwd. Helemaal links staan maximaal 7 cijfers, gevolgd door 2 cijfers en een controlegetal. Om het controlegetal te bepalen neemt men eerst de som van de getallen ervoor, telkens vermenigvuligd met hun rangnummer. Daarna bepaalt men de rest bij deling door 10.

Er geldt bijvoorbeeld voor **cafeïne**:

$$
\mathsf{1*8 + 2*0 +3*8+4*5 = 52}
$$

En inderdaad 52 heeft als rest 2 bij deling door 10.

Als extra voorbeeld: **Polypropeen** heeft als CAS nummer 9003-07-0. En inderdaad 

$$
\mathsf{1 * 7 + 2*0 + 3*3+4*0+5*0+6*9 = 70}
$$

wat rest 0 heeft bij deling door 10. Het controlegetal is dus inderdaad 0.

## Opgave

Schrijf een programma dat de eerste cijfers van het CAS-nummer vraagt en vervolgens het controlegetal uitrekent. Geef het vervolgens op de juiste manier weer.

#### Voorbeelden
Indien de gebruiker de code van cafeïne, `5808`, intikt, dan verschijnt er:

```
Het CAS-nummer is: 58-08-2
```

Indien de gebruiker de code van Polypropeen, `9000307`, intikt, dan verschijnt er:

```
Het CAS-nummer is: 9003-07-0
```

{: .callout.callout-info}
> #### Tips
> - Gebruik `//` en `%`.
> - Je kan voorloopnullen creëren via `zfill()`, bijvoorbeeld: `str( getal ).zfill(2)`. Dit zorgt ervoor dat `getal` steeds geschreven wordt met voorloopnullen tot er 2 tekens zijn. Indien `getal = 8` dan is het vorige gelijk aan `08`.
