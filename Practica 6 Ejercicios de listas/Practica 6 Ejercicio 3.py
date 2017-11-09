"""Jordi Vidal Palou. Pràctica 6.
Ejercicios de listas. Practica 6 ejercicio 3
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos
palabras y sustituya la primera por la segunda en la lista.  """

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
print "Substituye la palabra"
nombre1=raw_input()
print "por la palabra"
nombre2=raw_input()
while nombre1 in lista:
    a=lista.index(nombre1)
    lista.remove(nombre1)
    lista.insert(a, nombre2)
print lista

