{: .callout.callout-danger}
> #### Definitie
> Een natuurlijk getal (groter dan 1) is rechthoekig als je het kan schrijven als een **product** van twee opeenvolgende getallen.

Er geldt bijvoorbeeld dat 6 een rechthoekig getal is, want 6 is het product van 2 en 3. Ook 30 is een rechthoekig getal, want je kan het schrijven als een product van 5 en 6.

## Gevraagd
Schrijf een functie `is_rechthoekig( getal )`dat gegeven een natuurlijk getal groter dan 0 controleert of dit getal rechthoekig is.

Vraag vervolgens een bovengrens aan de gebruiker en druk alle rechthoekige getallen **kleiner** dan deze bovengrens af.

#### Voorbeelden
Voor invoer `12` verschijnt er:
```
6 is een rechthoekig getal.
```

Voor invoer `30` verschijnt er:
```
6 is een rechthoekig getal.
12 is een rechthoekig getal.
20 is een rechthoekig getal.
```

{: .callout.callout-info}
> #### Tip
> Gebruik eenzelfde principe als bij `is_priem()`... Het getal is **niet** rechthoekig **tot** je een deler vindt waarbij de voorwaarde klopt.
