"""Jordi Vidal Palou. Pràctica 6.
Ejercicios de listas. Practica 6 ejercicio 4
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista. """

lista= []
print "Dime cuantas palabras tiene tu lista"
numero=int(raw_input())
i=0
while i < numero:
    print "dime la palabra ", i+1
    palabra=raw_input()
    lista.append (palabra)
    i+= 1
print "La lista creada es", lista
print "Elimina la palabra"
nombre1=raw_input()
while nombre1 in lista:
    lista.remove (nombre1)
print lista

