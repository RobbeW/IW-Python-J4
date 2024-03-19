## Functies
In de vorige hoofdstukken heb je al verschillende functies gebruikt. Denk maar aan de in- en uitvoer functies `input()` en `print()`. In dit onderdeel ga je zelf functies schrijven. Waarom zou je zelf functies willen schrijven?

-   Er is een bepaalde functionaliteit die je op **meerdere** plekken in je programma nodig hebt, dan kan je die beter in een aparte functie stoppen in plaats van de code telkens te kopiëren.

-   Door functies met parameters te schrijven zal de code duidelijker worden, is deze **gemakkelijker te lezen** en te **onderhouden**.

-   Je programma is te lang om de inhoud goed te blijven overzien. Door de code op te splitsen in functies blijf je veel langer grip houden op de inhoud en werking.

-   ...

### Definitie
```python
def <functienaam>( <parameter_lijst>) :
    <acties>
```

{: .callout.callout-danger}
> #### Opgelet
> Zeer belangrijk in het aanmaken van een functie is de **indentatie**. Je merkt dat de acties in de functie naar rechts werden *opgeschoven* of *geïndenteerd*. Dat doe je gemakkelijk met behulp van de **tab** toets.

Hieronder zie je een voorbeeld van een functie. Deze functie bevat één parameter, namelijk `naam`. Door gebruik te maken van een functie wordt de code **dynamischer**. Je hoeft maar op één plaats iets aan te passen zodat er verschijnt `Goeiemorgen Jan !`. Wat wijzig je hiervoor?

```python
def begroeting( naam ):
    print( "Hallo", naam, "!" )

begroeting( "Jan" ) 
begroeting( "Piet" )
begroeting( "Joris" )
begroeting( "Korneel" )
```

Je kan eenvoudig een functie met meerdere **parameters** aanmaken, bijvoorbeeld:

```python
def vermenigvuldig( x, y ):
    resultaat = x * y
    print( "Het product van", x, "en", y, "is", resultaat )

vermenigvuldig( 2023 , 5278238 )
vermenigvuldig( 2, 3 )
```

#### Return

Parameters worden gebruikt om informatie van buiten de functie naar de functie toe te communiceren. Vaak wil je ook informatie vanuit de functie naar het programma buiten de functie toe communiceren. Daartoe dient het commando `return`.

Uit de wetten van Newton volgt de volgende formule voor de valafstand $$\mathsf{d}$$ van een object gedurende een tijd $$\mathsf{t}$$. Op aarde is de zwaarteveldsterkte $$\mathsf{g = 9.81 \frac{\text{m}}{\text{s}^2}}$$

$$
\mathsf{d = \dfrac{1}{2}\cdot g \cdot t^2}
$$

We kunnen de valafstand eenvoudig berekenen met behulp van een functie in Python. 
```python
def valafstand( t, g = 9.81 ):
    d = 1/2 * g * pow( t, 2 )
    return d

print( "Als een object 3 seconden valt, dan legt het", valafstand( 3 ), "m af.")
```
Je merkt dat alle complexiteit in de functie bevat zit en de `print`-opdracht zeer natuurlijk leest.

De toevoeging van `g = 9.81` bij de parameters zorgde ervoor dat $$\mathsf{g}$$ **standaard** de waarde $$\mathsf{9.81}$$ krijgt. Op de maan is dit slechts $$\mathsf{1,625 \frac{\text{m}}{\text{s}^2}}$$, zodat we de vorige zin bijvoorbeeld eenvoudig kunnen aanpassen. $$\mathsf{g}$$ was bij deze functie dus een *optionele* parameter.
```python
print( "Als een object 3 seconden valt op de maan, dan legt het", valafstand( 3, 1.625 ), "m af.")
```

## Opgave
Beschouw onderstaande code, deze bevat een kleine **foutje**. 

Corrigeer deze code zodat als uitvoer verschijnt:

```
Een driehoek met basis 4.5 cm en hoogte 1.0 cm heeft oppervlakte 2.25 cm².
```