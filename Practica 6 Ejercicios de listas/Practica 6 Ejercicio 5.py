"""Jordi Vidal Palou. Pràctica 6.
Ejercicios de listas. Practica 6 ejercicio 5
Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la
primera lista los nombres de la segunda lista.  """

lista1= []
lista= []
print "Dime cuantas palabras tiene tu lista"
numero=int(raw_input())
i=0
while i < numero:
    print "dime la palabra ", i+1
    palabra1=raw_input()
    lista1.append (palabra1)
    i+= 1
print "La lista creada es", lista1
print "Dime cuantas palabras tiene tu lista 2"
numero1=int(raw_input())
j=0
while j < numero1:
    print "dime la palabra ", j+1
    palabra=raw_input()
    lista.append (palabra)
    j+= 1
print "La lista creada es", lista
while palabra in lista1:
    lista1.remove (palabra)
print "la lista es ahora", lista1

