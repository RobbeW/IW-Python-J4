**Herhaling:**

Een **begrensde herhaling** is een herhaling van acties waarvan we weten, op voorhand (dus bij de fase van de analyse in het computationeel denken) hoeveel keer die uitgevoerd moet worden. Het aftellen bij verstoppertje, het verzamelen van 100 schelpen ... 

**Syntax:**

Voor een begrensde herhaling gebruiken we volgende syntax: 
for i in range() 
* i is de naam van een variabele (soms ook *teller* genoemd)
* De range()-operator heeft de volgende syntax:
* range(4) van 0 tot 4, 4 niet inbegrepen 
* range(3,6) van 3 to 6, 6 niet inbegrepen
* range(0,8,2) van 0 tot 8 met stapgrootte 2, 8 niet inbegrepen

**Gegeven:**

Elk jaar groeit de bevolking van België aan met 62770 inwoners. Dit door een combinatie van geboortecijfers (nataliteit die hoger ligt dan de mortaliteit) en immigratie. Momenteel 2022) zijn er 11.584.008 inwoners.

**Gevraagd:** 

Voor de begrotingsopmaak en de staatsschuld wil men berekenen hoeveel Belgen er zullen zijn in het jaar 2070. 
Schrijf de code die: 

* per jaar berekent hoeveel inwoners telt;
* wanneer het jaartal deelbaar is door tien, het jaartal en het aantal inwoners print op het scherm;
* het aantal inwoners in 2070 print op het scherm.  
* gebruik voor bij de print-functies verzorgde zinnen. 