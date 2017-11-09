"""Jordi Vidal Palou. Pràctica 6. Ejercicio 10
Escribe un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo). """

lista= []
print "Dime tu numero"
numero=int(raw_input())
for i in range (1, numero+1):
    if numero%i==0:
        lista.append (i)
print "La lista de numeros es", lista



