"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 5
Escriu un programa que te demani dos nombres cada vegada més grans i els guardi en una llista.
Per a terminar d'escriure els nombres, escriu un nombre que no sigui major a l'anterior. El
programa termina escribint la llista de nombres. """

lista = []
lista1 = []
print "Escribe un numero"
num1=raw_input()
lista1.append(float(num1))
a=0
print "Escribe un numero mayor que", num1
a=raw_input()
while num1 < a:
    lista.append(float(a))
    print "Escribe un numero mayor que", a
    a=raw_input()
print "Los numeros que has escrito son", lista1 + lista
