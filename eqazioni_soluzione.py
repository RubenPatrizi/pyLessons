from math import sqrt

a = int(input("Inserisci il valore di a: "))
b = int(input("Inserisci il valore di b: "))
c = int(input("Inserisci il valore di c: "))
delta = b**2 - 4*a*c

scelta = input("Determinare tipo o valore delle soluzioni? (Scrivere tipo o valore)\n")

if scelta == "tipo":
    if delta > 0:
        print("Soluzioni reali e distinte")
    if delta == 0:
        print("Soluzioni reali e coincidenti")
    if delta < 0:
        print("Soluzioni complesse e coniugate")

elif scelta == "valore":
    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print(f"Le soluzioni sono {x1} e {x2}")
    if delta == 0:
        x1 = -b / (2*a)
        print(f"Le soluzioni sono {x1} e {x1}")
    if delta < 0:
        print("Soluzioni complesse e coniugate, non posso calcolarle! :(")

else:
    print("Comando errato")
  
