"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 7
Escribe un programa que lea una frase, y la pase como par�metro a un procedimiento. El
procedimiento contar� el n�mero de vocales (de cada una) que aparecen, y lo imprimir� por
pantalla. """


lista=[]
print "Escribe una frase y te dir� cuantas vocales hay en ella"
frase=raw_input()
lista.append(frase)
vocales=["a","e","i","o","u"]
aux=0
for i in range(0, len(frase)):
    if frase[i] in vocales:
        aux = aux+1
print "vocales=", aux
        



