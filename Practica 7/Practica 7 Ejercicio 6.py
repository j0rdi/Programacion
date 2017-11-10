"""Jordi Vidal Palou. Pràctica 7. Ejercicio 6
Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una
función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo
imprimirá el programa principal por pantalla.  """


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
    print "Ese carácter está en tu nombre"
else:
    print "Ese carácter NO está en tu nombre"


