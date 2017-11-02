# -*- coding: cp1252 -*-
"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 3
Escriu un programa que demani notes i les guardi en una llista. Per a terminar d'introduir notes,
escriu una nota que no estigui entre 0 i 10. El programa termina escrivint la llista de notes."""


lista = []
print "Hola introduce una nota"
a=raw_input()
while a > 10:
    lista.append(float(a))
    print "Hola escribe una nota"
    a=raw_input()
print lista 
