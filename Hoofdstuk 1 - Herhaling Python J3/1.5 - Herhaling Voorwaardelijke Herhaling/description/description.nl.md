**Herhaling:**

Een **voorwaardelijke herhaling** is een herhaling van acties die blijft lopen **zolang** aan de voorwaarde wordt voldaan. Dus zolang de uitkomst van onze voorwaarde WAAR of TRUE is, zullen de acties onder de herhaling herhaald worden. 

Een voorbeeld van zo'n herhaling: 
* Je bent pannenkoek aan het bakken;
* Je laat die liggen totdat het deeg aan de bovenzijde niet meer lopend is;
* Met andere woorden: **zolang** het deeg lopend is, blijf je bakken; 
* Wanneer de toplaag niet meer lopend is, draai je deze om. 


**Syntax:**

Voor een voorwaardelijke herhaling gebruiken we volgende syntax: while voorwaarde: 

* while betekent zolang; 
* bij een voorwaarde gebruiken we een logische operator zoals > of !=; 
* we sluiten onze functie af met een dubbelpuntsteken; 
* alle acties die horen tot de herhaling laten we inspringen (de indent). 

while deeg != gestold: 
    bakken()
omdraaien() 

**Gegeven:**

Het belooft een heel warme zomerdag te worden. Men voorspelt dat het kwik in Ukkel, bij het meetcentrum, zal stijgen tot 37.9 graden Celcius. Om 08.00 uur bedraagt de temperatuur 18.4 graden Celcius. Elk uur is het 11% warmer dan het uur ervoor (lees: het is een exponentiële stijging). 

<img src="https://play-lh.googleusercontent.com/29fAV6TZJnKEmx-aeCM3ehOIbfv30ZB6E8lgycS2sDgzt_TKavB5TsCun4B7YhLN3Q"/>

**Gevraagd:**

* schrijf de code die de temperatuur elk uur berekent; 
* na elk uur verschijnt op het scherm "Om X uur is het T graden Celcius." 
* wanneer de temperatuur boven de 38 graden Celcius komt, stopt de code en verschijnt een alarm op het scherm. 
* het alarm: "De alarmtemperatuur werd bereikt. Het is momenteel X uur en de temperatuur bedraagt T graden Celcius."