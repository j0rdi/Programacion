# -*- coding: cp1252 -*-
"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 2
Escriu un programa que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres."""


lista = []
print "Hola introduce un numero"
a=raw_input()
while a!="":
    lista.append(int(a))
    print "Hola escribe un numero"
    a=raw_input()
print lista
    
    
