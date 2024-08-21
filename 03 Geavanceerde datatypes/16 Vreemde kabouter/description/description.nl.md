Volgens legendes wonen kabouters meestal onder de grond. Daar graven ze de wortels van planten op waardoor er hoopjes aarde in de tuin ontstaan. 

![Afbeelding door Craig McLachlan op Unsplash.](media/craig-mclachlan.jpg "Afbeelding door Craig McLachlan op Unsplash."){:data-caption="Afbeelding door Craig McLachlan op Unsplash." width="45%"}

Mevr. Wemel die dit allemaal vervelend vindt moet regelmatig haar tuin *ont-kabouteren* door ze over het hek te gooien. Dit is veel werk want ze gooit de kabouters één per één erover. Gelukkig zijn de kabouters zo volgzaam ten opzichte van hun koning, zodat indien de kabouter koning over het hek gegooid wordt, ze allemaal in één keer volgen.

Hoe kan mevr. Wemel de koning uit een groep kabouters vinden? Ze weet dat de kabouters altijd in een specifieke volgorde reizen, en dat de koning (speciaal als hij is), de enige kabouter is die de volgorde niet volgt. Enkele tips:

- Er is exact één koning in elke groep;
- Behalve de koning, reizen de kabouters in strikt stijgende volgorde volgens hun nummer;
- De koning is altijd de enige kabouter die niet op nummer loopt;
- De koning is nooit de eerste of de laatste in de groep, omdat hij zich graag verstopt.

Help mevr. Wemel om de koning te vinden!

## Opgave

Schrijf een functie `koning([nummers])` die gegeven een  lijst `nummers` op zoek gaat naar het **volgnummer** van de kabouter koning. Er zijn geen dubbele nummers terug te vinden en met uitzondering van de koning is elk nummer percies één meer dan het voorgaande nummer. Bestudeerd grondig onderstaande voorbeelden.

#### Voorbeelden

```python
>>> koning([1, 2, 3, 4, 8, 5, 6])
5
```
Het afwijkende nummer `8` staat immers op plaats 5.


```python
>>> koning([3, 4, 5, 2, 6])
4
```
Het afwijkende nummer `2` staat immers op plaats 4.

```python
>>> koning([10, 20, 11, 12])
2
```
Het afwijkende nummer `20` staat immers op plaats 2.

{: .callout.callout-secondary}
>#### Bron
> ICPC North American Qualifier Contest 2017