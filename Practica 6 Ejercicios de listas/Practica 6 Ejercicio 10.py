"""Jordi Vidal Palou. Pr�ctica 6. Ejercicio 10
Escribe un programa que pida un n�mero y a continuaci�n escriba la lista de todos los divisores
del n�mero (incluidos el uno y �l mismo). """

lista= []
print "Dime tu numero"
numero=int(raw_input())
for i in range (1, numero+1):
    if numero%i==0:
        lista.append (i)
print "La lista de numeros es", lista



