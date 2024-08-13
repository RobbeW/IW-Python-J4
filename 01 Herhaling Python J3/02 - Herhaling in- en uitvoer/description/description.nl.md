Binnen Python kan je aan een gebruiker **invoer** vragen via de `input()` functie.

```python
input('Geef je voornaam in:')
```

Deze invoer kan je vervolgens opslaan in een variabele. Een variabele op het scherm **weergeven** of printen kan via:

```python
print(variabele)
```

Om verschillende variabelen of teksten te **concateneren** gebruik je de uitgebreide `print()` functie.

```python
print(voornaam, naam)
```

Tekst kan je concateneren (zonder tussenliggende spatie) met behulp van een `+` teken.

```python
print("Hallo", voornaam + ".")
```

## Opgave
Schrijf een programma dat een **voornaam** en **leeftijd** (in jaren) vraagt. Vervolgens geeft het programma weer hoeveel dagen het nog duurt tegen dat de persoon 100 jaar wordt. Gebruik 365.25 dagen in één jaar om te compenseren voor de schrikkeljaren. **Rond af** op een geheel aantal dagen.


#### Voorbeelden

Voor achtereenvolgende invoer `Ward` en `16` jaar verschijnt er:
```
Ward, het duurt nog ongeveer 30681 dagen tot je 100 jaar bent!
```
