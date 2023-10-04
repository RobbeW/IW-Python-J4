#!/usr/bin/python
# -*- coding: utf-8 -*-

# invoer
u = int( input( 'Geef u in:' ) )
z = int( input( 'Geef z in:' ) )
vertrek = int( input( 'Geef vertrek in:' ) )
aankomst = int( input( 'Geef aankomst in:' ) )


# berekeningen
v = 4
if vertrek > 1:
    if vertrek <= 8:
        v = 5
    elif vertrek <= 12:
        v = 0
    elif vertrek <= 18:
        v = 1
    elif vertrek <= 22:
        v = 3

a = 1
if aankomst > 1:
    if aankomst <= 8:
        a = 3
    elif aankomst <= 12:
        a = 4
    elif aankomst <= 18:
        a = 2
    elif aankomst <= 22:
        a = 0

d = round( ((u / 2)+z-3+v+a) / 10, 2)

# uitvoer
print('')
print('Je hebt', d, 'dagen nodig om te herstellen.')