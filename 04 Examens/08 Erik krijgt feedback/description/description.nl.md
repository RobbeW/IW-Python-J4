## Gegeven
Erik gaat naar school in Gent waar de leerlingen regelmatig toetsen maken en hier achteraf feedback uit krijgen. De leerkracht van Erik is het wel nogal beu om altijd hetzelfde commentaar te schrijven en probeert een programma te maken om deze feedback vanzelf te krijgen.

![Erik krijgt feedback.](media/feedback_schrijven.jpg "Erik krijgt feedback."){:data-caption="Erik krijgt feedback." width="45%"}

## Opgave
Schrijf een programma dat aan de leerkracht de naam van de leerling en de score (op 20) meegeeft. Je krijgt daarna volgende berichtgeving: 
- Als de leerling meer dan 13 scoort en maximaal 17, is de feedback: "Beste [naam], dit is een goed resultaat. Doe zo voort!" 
- Als de leerling minder dan 10 scoort komt er: "Je behaalt een onvoldoende voor deze toets [naam], je krijgt van mij een remediëring."
- Als de leerling minstens 17 scoort verschijnt er: "Wat een subliem resultaat! Met een [score] bewijs je talent te hebben voor dit vak!" 
- In alle andere situaties krijgt de leerling: "Je behaalt een voldoende [naam], maar zal je toch moeten herpakken. Herhaal deze leerstof en maak meer oefeningen voor het examen!"

#### Voorbeelden

`Erik` behaalt een `7.5`:
```
Je behaalt een onvoldoende voor deze toets Erik, je krijgt van mij een remediëring.
```


`Fred` behaalt een `15`:
```
Beste Fred, dit is een goed resultaat. Doe zo voort!
```