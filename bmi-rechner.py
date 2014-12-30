### BMI-Rechner
### Thomas Hirmer
### 30-12-2014


### Eingabe ###
print("Bitte geben Sie ihr Gewicht in Kg ein: ")
gewicht=float(input())

print("Bitte geben Sie Ihre Körpgergrösse in cm ein: ")
groesse=float(input())
groesse=groesse/100.00


'''print ("Sind sie männlich(m) oder Weiblich(w)? ")
gender=input()'''

### Verarbeitung ###
bmi=gewicht/(groesse*groesse)

### Ausgabe ###
print("Ihr BMI beträgt " + str(bmi))
if bmi < 16:
    print("Starkes Untergewicht!")
elif 16 <= bmi < 17:
    print("Maessiges Untergewicht!")
elif 17 <= bmi < 18.5:
    print("Leichtes Untergewicht!")
elif 18.5 < bmi < 25:
    print("Sie haben Normalgewicht! Herzlichen Glueckwunsch!")
elif 25 <= bmi < 30:
    print("Sie befinden sich im Praeadipositas-Bereich.")
elif 30 <= bmi < 35:
    print("Adipositas Grad I")
elif 35 <= bmi < 40:
    print("Adiposiats Grad II")
elif bmi >= 40:
    print("Adipositas Grad III")
else:
    print("Programmfehler: Fall nicht definiert.")