### BMI-Rechner
### Thomas Hirmer
### 30-12-2014


### Eingabe ###
print("Bitte geben Sie ihr Gewicht in Kg ein: ")
gewicht=int(input())

print("Bitte geben Sie Ihre Körpgergrösse in Meter ein: ")
groesse=float(input())


### Verarbeitung ###
bmi=gewicht/(groesse*groesse)


### Ausgabe ###
ausgabe=str(bmi)
print("Ihr BMI betraegt: "+ ausgabe)
