Elke jongere die op zijn/haar/hun budget wil letten tijdens het reizen, maakt best gebruik van een jeugdherberg. Daar zijn meestal goedkope slaapzalen, waar je met medereizigers naast elkaar slaapt.

Het juiste bed kiezen kan het verschil maken tussen een goede nachtrust of nauwelijks een oog te kunnen sluiten. De afstand tot de dichtste medereiziger blijkt hiervoor cruciaal. Naast iemand slapen die snurkt is immers nefast voor je humeur.

![Gesnurk van Homer Simpson.](media/simpsons.gif "Gesnurk van Homer Simpson."){:data-caption="Gesnurk van Homer Simpson." width="200px"}

## Gevraagd
Schrijf een functie `aantal_links(bedden)` dat gegeven een lijst van slaapplekken een nieuwe lijst retourneert met het aantal lege bedden links van elke positie, tot de volgende bezette slaapplek. Op de plaats van de bezette bedden plaats je `0`. Indien er geen bezet bed is aan de linkerkant plaats je `-1`. Op de plaats van een leeg bed neem je dat bed zelf mee in het aantal bedden.

Bestudeer grondig onderstaande voorbeelden.

#### Voorbeelden

```python
>>> aantal_links([".", "X", ".", "X", "."])
[-1, 0, 1, 0, 1]
```

```python
>>> aantal_links([".", "X", ".", ".", ".", "X", "."])
[-1, 0, 1, 2, 3, 0 ,1]
```

```python
>>> aantal_links([".", "X", ".", ".", ".", ".", "X"])
[-1, 0, 1, 2, 3, 4, 0]
```

```python
>>> aantal_links([".", ".", ".", "X"])
[-1, -1, -1, 0]
```