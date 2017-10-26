# -*- coding: cp1252 -*-
"""JORDI VIDAL PALOU - 1º DAW - PRACTICA4 - EJERCICIO 8
Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:"""

print "Dime la altura de tu triángulo"
altura=int(raw_input())
for i in range(1,altura+1):
    print "*"*i
for i in range(altura-1,0,-1):
    print "*"*i
    
