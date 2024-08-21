## Lijsten

Een lijst is een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Lijsten worden gedefinieerd met vierkante haakjes `[  ]` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de lijst.

```python
lijst = ["banaan", "appel", "peer"]
print(lijst)          # Dit print ["banaan", "appel", "mango"]
print(len(lijst))     # Dit print 3, want de lijst bevat 3 elementen
```

Hier zie je een lijst met drie elementen, telkens van het datatype `string`. Je kan gemakkelijk de elementen van deze lijst apart bewerken, dat doe je met behulp van de rangnummers.

```python
lijst = ["banaan", "appel", "peer"]
print(lijst[0])       # Dit print "banaan"
lijst[2] = "mango"    # Wijzigt het laatste element van de lijst
print(lijst)          # Dit print ["banaan", "appel", "mango"]
```

{: .callout.callout-danger}
> #### Opgelet
> Merk op dat het **eerste** element van de lijst rangnummer `0` heeft!

## Opgave
Het onderstaande programma verwisselt het eerste en laatste element in een lijst. 
Toch bevat dit programma een **foutje**, kan je het aanpassen?

#### Voorbeeld

```python
>>> verwissel(["Cédric", "Luiz", "Ward", "Briek", "Miel"])
["Miel", "Luiz", "Ward", "Briek", "Cédric"]
```