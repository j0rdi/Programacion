"""JORDI VIDAL PALOU - 1º DAW - PRACTICA4 - EJERCICIO 4
Escriu un programa que demani un nombre i calculi el seu factorial."""


print "Dime un numero"    
numero=int(raw_input())
factorial= 1
for i in range(1,numero+1):
    factorial = (factorial * i)
    print i
print "El factorial de" ,numero, "es" ,factorial


    


