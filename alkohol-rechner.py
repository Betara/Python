### Berechnet die Menge an Alkohol in mg
### Thomas Hirmer
### 30-12-2014


### Eingabe ###
print("Die Menge des Getränks in ml: ")
z = input()
volumen=int(z)

print("Der Alkoholgehalt in Volumenprozent (Vol.-%): ")
z = input()
alkoholgehalt = float(z)


### Verarbeitung ###
ergebnis = volumen * (alkoholgehalt/100) * 0.8

### Ausgabe ###
print("In dem Getränk ist folgende Menge in g an Alkohol enthalten: " + str(ergebnis))