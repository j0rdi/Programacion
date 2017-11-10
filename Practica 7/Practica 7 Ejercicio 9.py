"""Jordi Vidal Palou. Pràctica 7. Ejercicio 9
Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si
riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman. """


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
            


        



