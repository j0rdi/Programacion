"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 4
Escriu un programa que te demani dos nombres, de manera que el segon sigui major que el
primer. El programa termina escrivint els dos nombre tal i com es demana. """


print "Escribe un numero"
num1=raw_input()
print "Escribe un numero mayor que", num1
num2=raw_input()
while num2 < num1:
    print "El" ,num2, "es menor que" ,num1, 
    print "Vuelve a introducir un numero mayor que", num1
    num2=raw_input()
print "Los numeros que has escrito son" ,num1, "y" ,num2
