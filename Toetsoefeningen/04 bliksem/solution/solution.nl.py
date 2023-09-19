#!/usr/bin/python
# -*- coding: utf-8 -*-

tijd = int( input( 'Geef het aantal seconden in:' ) )

afstand = round( ( tijd * 343 ) / 1000, 3 )

print()
print( 'De blikseminslag was', afstand, 'km van je verwijderd.' )