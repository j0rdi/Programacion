print "Convertidor de segundos a horas y minutos. Escribe una cantidad de segundos"
segundos = int(raw_input())
horas= (segundos // 3600)
minu= (segundos % 3600) //60
segun= segundos % 60

print segundos, "segundos son" ,horas, "horas" , minu , "minutos y", segun, "segundos"
