"""JORDI VIDAL PALOU - 1� DAW - PRACTICA4 - EJERCICIO 9
Escriu un programa que demani l'amplada i l'al�ada d'un rectangle i ho dibuixi de la seg�ent
manera:"""

print "Dime el ancho de tu rect�ngulo"    
ancho=int(raw_input())
print "Dime la altura de tu rect�ngulo"
altura=int(raw_input())
for i in range(altura):
    for j in range(ancho):
        if (i==0) or (i==altura-1):
            print "*",
        else:
            if (j==0) or (j==ancho-1):
                print "*",
            else:
                print " ",
    print ""
        
