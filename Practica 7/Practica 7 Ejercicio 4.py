"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 4
Escribe un programa que pida una frase, y le pase como par�metro a una funci�n dicha frase. La
funci�n debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla. """

lista=[]
print "Dime una frase"
a=raw_input()
lista.append(a)
a=list(a)
print a
while ' ' in a:
    paco=a.index(' ')
    a.remove(' ' )
    a.insert(paco, '*')
print a
    

 





