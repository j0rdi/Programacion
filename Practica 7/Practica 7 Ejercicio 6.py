"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 6
Escribe un programa que lea el nombre de una persona y un car�cter, le pase estos datos a una
funci�n que comprobar� si dicho car�cter est� en su nombre. El resultado de dicha funci�n lo
imprimir� el programa principal por pantalla.  """


lista=[]
print "Dime tu nombre"
frase=raw_input()
lista.append(frase)
frase=list(frase)
print frase
print "Dime un caracter"
carac=raw_input()
lista.append(carac)
if carac in lista:
    print "Ese car�cter est� en tu nombre"
else:
    print "Ese car�cter NO est� en tu nombre"


