"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 8
Escribe un programa que pida una frase, y pase la frase como par�metro a una funci�n que debe
eliminar los espacios en blanco (compactar la frase). El programa principal imprimir� por pantalla
el resultado final. """


lista=[]
print "Dime una frase"
a=raw_input()
lista.append(a)
a=list(a)

while ' ' in a:
    a.remove(' ' )
    
print ''.join(a)
        



