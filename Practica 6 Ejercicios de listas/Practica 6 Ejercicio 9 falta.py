"""Jordi Vidal Palou. Pràctica 6. Ejercicio 9
Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista con las palabras de la primera, pero sin palabras repetidas (el orden de las palabras
en la segunda lista no es importante).  """

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
c=0
lista2 = []
for j in range(numero):
    if palabra in lista:
        lista2.append(palabra)
        c+=1   
print "La lista sin repeticiones es", lista2




