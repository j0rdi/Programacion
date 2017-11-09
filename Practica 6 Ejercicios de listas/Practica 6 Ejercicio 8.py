"""Jordi Vidal Palou. Pràctica 6. Ejercicio 8
Escribe un programa que permita crear una lista de palabras y que, a continuación, ordene la lista
por orden alfabético. """

lista= []
print "Dime cuantas palabras tiene tu lista"
numero=int(raw_input())
i=0
while i < numero:
    print "dime la palabra ", i+1
    palabra=raw_input()
    lista.append (palabra),
    i+= 1
    
a = lista
b = sorted(a)
print "La lista creada es", lista
print "La lista ordenada es", b




