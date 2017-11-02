"""Jordi Vidal Palou Pràctica 5.
Exercicis while i llistes. Practica 5 ejercicio 9
Escriu un programa que et demani noms de persones i els seus números de telèfon. Per a
terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
termina escribint noms i números de telèfon. Nota: La llista en la que es guarden els noms i
números de telèfon és [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc] """

lista = []
lista1 = []
print "Dame un nombre"
num1=raw_input()
lista1.append(float(num1))
a=0
print "Escribe un numero mayor que", num1
a=raw_input()
while num1 < a:
    lista.append(float(a))
    print "Escribe un numero mayor que", a
    a=raw_input()
print "Los numeros que has escrito son", lista1 + lista

