"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 5
Escribe un programa que te pida una frase y una vocal, y pase estos datos como par�metro a una
funci�n que se encargar� de cambiar todas las vocales de la frase por la vocal seleccionada.
Devolver� la funci�n la frase modificada, y el programa principal la imprimir�: """


lista=[]
print "Dime una frase"
frase=raw_input()
lista.append(frase)
frase=list(frase)
print frase
print "Dime una vocal"
vocal=raw_input()
vocales=["a","e","i","o","u"]
aux=0
while vocales in lista:
    lista.replace(vocales, vocal)
print lista


