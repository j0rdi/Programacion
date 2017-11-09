"""Jordi Vidal Palou. Pràctica 6. Ejercicio 7
Escribe un programa que permita crear dos listas de palabras y que, a continuación, escriba las
siguientes listas (en las que no debe haber repeticiones):
• Lista de palabras que aparecen en las dos listas
• Lista de palabras que aparecen en la primera lista, pero no en la segunda
• Lista de palabras que aparecen en la segunda lista, pero no en la primera
• Lista de palabras que aparecen en ambas listas """

lista= []
print "Dime cuantas palabras tiene tu lista"
numero=int(raw_input())
i=0
while i < numero:
    print "dime la palabra ", i+1
    palabra=raw_input()
    lista.append (palabra)
    i+= 1       
print "La primera lista creada es", lista
lista2= []
print "Dime cuantas palabras tiene tu lista"
numero2=int(raw_input())
j=0
while j < numero2:
    print "dime la palabra ", j+1
    palabra2=raw_input()
    lista2.append (palabra2)
    j+= 1       
print "La segunda lista creada es", lista2
comun=[]
while palabra==palabra2:
    comun.append (palabra3)
    i+= 1
    print comun





