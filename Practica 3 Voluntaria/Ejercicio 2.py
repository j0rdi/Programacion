print "Hola, te voy a decir tu indice de masa corporal, dime cuanto pesas en kg"
kg = float(raw_input())
print "Dime cuanto mides en metros"
altura = float(raw_input())
print "Tu indice de masa corporal IMC es" , kg/(altura**2)
if kg/(altura**2)>25:
    print "Un imc muy alto indica obesidad. Los valores 'normales' de imc están entre 20 y 25"
if kg/(altura**2)>19:
    print "Estas en el imc ideal. Los valores 'normales' de imc están entre 20 y 25"
if kg/(altura**2)<=19:
    print "Un imc muy bajo indica delgadez. Los valores 'normales' de imc están entre 20 y 25"
    
