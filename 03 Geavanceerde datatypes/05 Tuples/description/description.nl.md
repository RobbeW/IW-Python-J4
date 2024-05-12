## Tupels

Een tupel is ook een **geordend** datatype dat meerdere elementen kan bevatten van een ander datatype. Dit datatype wordt gedefinieerd met behulp van `( )` en kommas tussen de elementen. Via `len()` bepaal je de lengte van de tupel. 

```python
tupel = ( -5, 6, 8 )
print( tupel )         # Dit print (-5, 6, 8)
print( len( tupel ) )  # Dit print 3, want de tupel bevat 3 elementen
```

Tupels zijn zeer gelijkaardig als lijsten, ze worden vooral gebruikt om met coördinaten te werken.

```python
A = (1, 3)
print( 'Punt A heeft x-coördinaat', A[0], 'en y-coördinaat', A[1] )
```

Het belangrijkste **verschil** met lijsten is dat je ze *niet meer kan aanpassen* eenmaal aangemaakt.


## Opgave
De (Euclidische) afstand $$\mathsf{d}$$ van de oorsprong tot een punt $$\mathsf{P(x,y)}$$ wordt gegeven door de volgende formule:

$$
    \mathsf{d = \sqrt{x^2+y^2}}
$$

Vul onderstaande functie `afstand(coordinaat)` aan die de afstand van een bepaalde coördinaat tot de oorsprong berekent. Rond hierbij af op 2 cijfers.

#### Voorbeeld

```
>>> afstand( (3.0,4.0) )
5.0
```
