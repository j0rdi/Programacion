"""JORDI VIDAL PALOU - 1º DAW - PRACTICA4 - EJERCICIO 2
Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins són
senars (=”impares”) des del primer fins al segon."""


print "Dime un numero"    
numero=int(raw_input())
print "Dime un numero mayor que", numero
mayor=int(raw_input())
for i in range(numero,mayor+1):
    print i
    if i%2 == 0:
        print "Este numero es par"
    else:
        print "Este numero es impar"
