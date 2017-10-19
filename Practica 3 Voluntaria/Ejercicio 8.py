print "Convertidor a gruesas y docenas. Escribe una cantidad ( entera):"
entero = int(raw_input())
gruesas= (entero // 144)
docenas= (entero % 144) //12
unidades= entero % 12

print entero, "son" ,gruesas, "gruesas" , docenas , "docenas y", unidades, "unidades"
