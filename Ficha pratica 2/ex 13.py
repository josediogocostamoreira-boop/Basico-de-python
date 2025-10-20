#horas

horas = int(input("introduza as horas:"))

minutos = int(input("introduza os minuto:"))

#conversão

if minutos == 60: horas = horas + 1

if minutos == 60: minutos = minutos - 60

if horas > 12 : print(horas -12 , minutos, "PM")

if horas <= 12 : print(horas , minutos, "AM")

