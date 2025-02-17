<a href="https://nl.wikipedia.org/wiki/Mexicanen_(dobbelspel)" target="_blank">Mexen</a> is a game of dice played by 2 people. Each roll consists of 2 dice. The game mostly consists of bluffing about your dice, but here we're only focussing on the scoring. Contrary to a lot of other dice games, your points don't just equal the sum of your dice rolls.

![Image by Edge2Edge Media on Unsplash.](media/edge2edge-media.jpg "Image by Edge2Edge Media on Unsplash."){:data-caption="Image by Edge2Edge Media on Unsplash." width="35%"}

Instead, the scoring works as follows:
- A *Mex* always lands you the most points, namely 1000;

  <span class="mdi mdi-36px mdi-dice-1-outline"></span> <span class="mdi mdi-36px mdi-dice-2-outline"></span> or <span class="mdi mdi-36px mdi-dice-2-outline"></span> <span class="mdi mdi-36px mdi-dice-1-outline"></span>

- After those, we have the doubles, like

  <span class="mdi mdi-36px mdi-dice-4-outline"></span> <span class="mdi mdi-36px mdi-dice-4-outline"></span>, ...

  If both players have a duplicate, the player with the higher pair wins, as your points equal the rolled result times 100.

- In any other case the rolls get sorted so the higher result is put first. The rolls as pictured below would result in a score of 43.

  <span class="mdi mdi-36px mdi-dice-4-outline"></span>  <span class="mdi mdi-36px mdi-dice-3-outline"></span>

## Assignment

Create a function `mexen(s0, s1, t0, t1)` that determines the winner, where `s0` and `s1` are the rolls of player 1 and `t0` and `t1` belong to player 2. If player 1 wins, you return `"speler 1"`, if player 2 wins, you return `"speler 2"` and otherwise you return `"gelijkspel"` (it's a tie).

To create this function you first create a helper function, `score(worp1, worp2)`, which determines the score of a single player given 2 rolls. 

Take a look at the examples below:

#### Examples

```python
>>> mexen(1, 2, 1, 3)
speler 1
```
because
```python
>>> score(1, 2)
1000
>>> score(1, 3)
31
```


```python
>>> mexen(3, 3, 2, 1)
speler 2
```
because
```python
>>> score(3, 3)
300
>>> score(2, 1)
1000
```


```python
>>> mexen(6, 6, 2, 2)
speler 1
```
because
```python
>>> score(6, 6)
600
>>> score(2, 2)
200
```


```python
>>> mexen(4, 2, 2, 4)
gelijkspel
```
because
```python
>>> score(4, 2)
42
>>> score(2, 4)
42
```

{: .callout.callout-secondary}
>#### Source
> Virginia Tech High School Programming Contest 2014
