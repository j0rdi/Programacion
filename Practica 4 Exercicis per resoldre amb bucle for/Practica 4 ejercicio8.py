# -*- coding: cp1252 -*-
"""JORDI VIDAL PALOU - 1� DAW - PRACTICA4 - EJERCICIO 8
Escriu un programa que demani l'al�ada d'un triangle i ho dibuixi de la seg�ent manera:"""

print "Dime la altura de tu tri�ngulo"
altura=int(raw_input())
for i in range(1,altura+1):
    print "*"*i
for i in range(altura-1,0,-1):
    print "*"*i
    
