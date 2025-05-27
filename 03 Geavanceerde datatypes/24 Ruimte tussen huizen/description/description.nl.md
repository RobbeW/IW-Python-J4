Stel dat je een lijst hebt met huizen 🏡 en spaties. Maak een nieuwe lijst dat het aantal spaties **links** van elke huis telt, **tot** je opnieuw een huis ontmoet.

Beschouw bijvoorbeeld de lijst `["🏡", " ", " ", "🏡", " ", "🏡"]` dan zou het bovenstaande probleem resulteren in de lijst `[0, 0, 1, 2, 0, 1]`. Want:

- links van het allereerste huis is er geen spatie te vinden;
- links van de eerste spatie staat enkel een huis;
- links van de tweede spatie staat één enkele spatie;
- links van het tweede huis staan twee spaties;
- links van de volgende spatie (tussen die spatie en het eerste huis) staan geen spaties;
- links van het laatste huis (tot het volgende huis) staat één enkele spatie.

## Opgave

Programmeer een functie `vrije_ruimte_links(lijst)` dat voor zo'n gegeven lijst het aantal spaties links van elk huis telt (tot je opnieuw een huis tegenkomt). Retourneer deze nieuwe lijst.

#### Voorbeelden
Bestudeer onderstaande voorbeelden grondig.

```python
>>> vrije_ruimte_links(["🏡", " ", " ", "🏡", " ", "🏡"])
[0, 0, 1, 2, 0, 1]
```

```python
>>> vrije_ruimte_links([" ", " ", " ", "🏡", " ", " ", "🏡"])
[0, 1, 2, 3, 0, 1, 2]
```