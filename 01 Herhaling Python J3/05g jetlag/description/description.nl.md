Iedereen die ooit al eens een lange vlucht naar het oosten of het westen heeft gemaakt, kent ongetwijfeld het fenomeen van de jetlag. Overdag voel je je moe en wil je gaan slapen, en 's nachts lig je wakker in bed. Na enkele dagen heb je je bioritme echter volledig aangepast aan de lokale omstandigheden. Om te berekenen hoeveel dagen $$\mathsf{d}$$ je nodig hebt om te herstellen van een jetlag, ontwikkelde de Internationale Burgerluchtvaartorganisatie (<a href="https://www.icao.int/Pages/default.aspx" target="_blanc">ICAO</a>) de volgende formule:

$$\mathsf{d = \frac{\frac{u}{2} + (z-3) + v + a}{10}}$$

Hierbij stelt $$\mathsf{u}$$ het aantal vlieguren van de reis voor en $$\mathsf{z}$$ het aantal tijdszones dat daarbij overbrugd wordt. Het uur van vertrek $$\mathsf{v}$$ en aankomt $$\mathsf{a}$$ wordt ingecalculeerd op basis van onderstaande tabellen.

| vertrek tussen | $$\mathsf{v}$$ | | aankomst tussen | $$\mathsf{a}$$ |
|:--------:|:-----------:|--|:--------:|:-----------:|
| 8u00 en 12u00 | 0| | 8u00 en 12u00 | 4|
| 12u00 en 18u00 | 1 | | 12u00 en 18u00 | 2 |
| 18u00 en 22u00| 3 | | 18u00 en 22u00| 0 |
| 22u00 en 1u00 | 4 | | 22u00 en 1u00 | 1 |
| 1u00 en 8u00 | 5 | | 1u00 en 8u00 | 3 |
{:class="table table-striped table-condensed" style="width:auto;margin-left:auto;margin-right:auto;"}


De grenzen die gebruikt worden om $$\mathsf{v}$$ en $$\mathsf{a}$$ te bepalen zijn steeds **exclusief het beginuur en inclusief het einduur**. Vertrek- en aankomsttijden zijn steeds aangegeven in de lokale tijd.

![Slaap inhalen op de luchthaven.](media/joyce-romero.jpg "Foto door Joyce Romero op Unsplash."){:data-caption="Slaap inhalen op de luchthaven." width="50%"}

## Opgave
Schrijf een programma dat vier natuurlijke getallen **vraagt**, respectievelijk de waarden voor $$\mathsf{u}$$, $$\mathsf{z}$$, vertrektijd en aankomsttijd.  De vertrek- en aankomsttijden worden afgerond tot het dichtsbijzijnde uur.

Daarna geeft het programma het aantal dagen dat nodig is om te herstellen van de jetlag weer.

#### Voorbeelden
Stel bijvoorbeeld dat je van New York Kennedy Airport naar London Heathrow vliegt. Je vlucht vertrekt om 7:00 lokale tijd in New York en komt aan om 19:00 lokale tijd in Londen. Als we weten dat het in Londen vijf uur later is dan in New York, dan hebben we dus als invoer de waarden `u=7`, `z=4`, `7` en `19`. (Wat overeenkomt met `v=5` en `a=0`.)
Wat als uitvoer oplevert:
```
Je hebt 0.95 dagen nodig om te herstellen.
```

Stel dat je vertrekt om 23u00 en de dag nadien om 21u00 aankomt. Onderweg ben je 7 tijdzones gepasseerd en de vlucht duurde dus 10 uur, dan leidt de invoer van `10`, `7`, `23` en `21` tot:
```
Je hebt 1.3 dagen nodig om te herstellen.
```