"""Jordi Vidal Palou. Pràctica 6.
Ejercicios de listas. Practica 6 ejercicio 1
Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
programa tiene que escribir la lista.  """

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

