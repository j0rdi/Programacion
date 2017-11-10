"""Jordi Vidal Palou. Pràctica 7. Ejercicio 2
Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver
una única cadena. La cadena final la imprimirá el programa por pantalla.
"""

def unir(a,b,c):
    return a+" "+b+" "+c
    


print "Dime tu nombre"
a=raw_input()
print "Dime tu primer apellido"
b=raw_input()
print "Dime tu segundo apellido"
c=raw_input()

resultado=unir(a,b,c)
print resultado

