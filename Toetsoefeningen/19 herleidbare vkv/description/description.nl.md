Een **volledige** vierkantsvergelijking is een vergelijking van de vorm:

$$\mathsf{ ax^2+bx+c = 0 \qquad \text{met } a\not = 0, b\not = 0, c \not = 0}$$

Bij sommige vierkantsvergelijkingen is de veelterm van de tweede graad te schrijven als een **kwadraat van een som**. Beschouw bijvoorbeeld het onderstaande voorbeeld:

$$
    \mathsf{ 4x^2 -12x + 9 = 0 \qquad \Leftrightarrow \qquad (2x-3)^2 = 0}
$$

De vierkantsvergelijking $$\mathsf{ 4x^2 -12x + 9 = 0}$$ kan dus **herleid** worden naar de eenvoudigere vorm $$\mathsf{ (2x-3)^2 = 0}$$.

Bevat het linkerlid het tegengestelde, dan kan deze ook herleid worden. Zo geldt:

$$
    \mathsf{ -4x^2 +12x -9 = 0 \qquad \Leftrightarrow \qquad -(4x^2 -12x +9) = 0 \qquad \Leftrightarrow \qquad -(2x-3)^2 = 0}
$$

## Opgave

Schrijf een programma dat voor een gegeven volledige vierkantsvergelijking **in volgorde** naar de coefficienten $$\mathsf{a}$$, $$\mathsf{b}$$ en $$\mathsf{c}$$ vraagt en nadien op het scherm weergeeft of de bijbehorende vierkantsvergelijking te herleiden valt.

Het is **niet toegelaten** in deze oefening om de discrimant uit te rekenen.

#### Voorbeelden
Voor vierkantsvergelijking $$\mathsf{ 4x^2 -12x + 9 = 0}$$ verschijnt er:
```
Deze vkv kan meteen naar een kwadraat herleid worden.
```

Voor vierkantsvergelijking $$\mathsf{ 4x^2 -6x + 9 = 0}$$ verschijnt er:
```
Deze vkv kan niet naar een kwadraat herleid worden.
```

Voor vierkantsvergelijking $$\mathsf{ 4x^2 +12x - 9 = 0}$$ verschijnt er:
```
Deze vkv kan niet naar een kwadraat herleid worden.
```

{: .callout.callout-info}
> #### Tips
> - Noteer zelf nog een ander voorbeeld van een vierkantsvergelijking die te herleiden valt.
> - Je mag er van uit gaan dat de coëfficienten steeds geheel zijn.
> - Gebruik `import math`.
> - De coëfficienten kunnen negatief zijn... Hou daarmee, indien nodig, rekening.

