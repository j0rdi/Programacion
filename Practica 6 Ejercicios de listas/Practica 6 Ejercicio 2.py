"""Jordi Vidal Palou. Pràctica 6.
Práctica 6. Ejercicios de listas.Practica 6 ejercicio 2
Ejercicio 02
Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista. 
"""

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
print "Dime la palabra y te diré cuantas veces sale en la lista ;)"
pal=raw_input()
c=0
for j in range(numero):
    if pal in lista:
        lista.remove(pal)
        c+=1     
print pal, "está en la lista" ,c, "veces"
