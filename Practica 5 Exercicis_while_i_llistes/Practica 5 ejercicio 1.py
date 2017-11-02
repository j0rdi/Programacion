# -*- coding: cp1252 -*-
"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 1
Escriu un programa que te demani paraules i les guardi en una llista.
Per a terminar d'introduir paraules, simplement pitja Enter.
El programa termina escribint la llista de paraules.  """


lista = []
print "Hola introduce una palabra"
a=raw_input ()
while a:
    lista.append(a)
    print "Hola escribe una palabra"
    a=raw_input ()
print lista
