"""Jordi Vidal Palou. Pr�ctica 6. Ejercicio 6
Escribe un programa que permita crear una lista de palabras y que, a continuaci�n, cree una
segunda lista igual a la primera, pero al rev�s (no se trata de escribir la lista al rev�s, sino de crear
una lista distinta).  """

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
listainv= []
for z in lista:
    listainv = [z]+listainv
print "La lista inversa es", listainv 




