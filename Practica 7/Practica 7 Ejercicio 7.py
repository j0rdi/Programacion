"""Jordi Vidal Palou. Pràctica 7. Ejercicio 7
Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El
procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por
pantalla. """


lista=[]
print "Escribe una frase y te diré cuantas vocales hay en ella"
frase=raw_input()
lista.append(frase)
vocales=["a","e","i","o","u"]
aux=0
for i in range(0, len(frase)):
    if frase[i] in vocales:
        aux = aux+1
print "vocales=", aux
        



