"""JORDI VIDAL PALOU - 1º DAW - PRACTICA4 - EJERCICIO 3
Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
fins al segon."""


print "Dime un numero"    
numero=int(raw_input())
print "Dime un numero mayor que", numero
mayor=int(raw_input())
suma= 0
for i in range(numero,mayor+1):
    suma = suma + i
    print i
print "La suma desde", numero,"hasta", mayor,"es", suma
    
    
