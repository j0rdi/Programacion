"""Jordi Vidal Palou. Pr�ctica 7. Ejercicio 9
Escribe un programa que pida dos palabras las pase como par�metro a un procedimiento y diga si
riman o no. Si coinciden las tres �ltimas letras tiene que decir que riman. Si coinciden s�lo las dos
�ltimas tiene que decir que riman un poco y si no, que no riman. """


lista=[]
print "Dime la primera palabra"
a=raw_input()
lista.append(a)
listab=[]
print "Dime la segunda palabra"
b=raw_input()
listab.append(b)
if a[-3:] == b[-3:]:
    print "Las palabras", a, "y" , b, "riman!"
else:
    if a[-2:] == b[-2:]:
        print "Las palabras", a, "y" , b, "riman un poco"
    else:
        print "Las palabras", a, "y" , b, "No riman!"
            


        



