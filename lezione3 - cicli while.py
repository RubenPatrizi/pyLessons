# I cicli while consentono di ripetere delle istruzioni finché è verificata una certa condizione.
# Questa condizione viene espressa analogamente a quanto già visto per il costrutto if.
# Ad esempio se volessimo chiedere all'utente di inserire 3 parole dovremmo scrivere

parola1 = input("Inserisci una parola: ")
print("La parola inserita è lunga %d caratteri" % len(parola1))    # la funzione len() restituisce la lunghezza della stringa
parola1 = input("Inserisci una parola: ")                            # ovvero il numero di caratteri che la compongono
print("La parola inserita è lunga %d caratteri" % len(parola1))
parola1 = input("Inserisci una parola: ")
print("La parola inserita è lunga %d caratteri" % len(parola1))

print("-"*15)

# Per evitare ripetizioni di codice possiamo sfruttare un ciclo while che, ad esempio, viene ripetuto 3 volte

i = 0
while i < 3:
    parola1 = input("Inserisci una parola: ")
    print("La parola inserita è lunga %d caratteri" % len(parola1))
    i = i + 1

# Creiamo una variabile i che tiene conto di quante ripetizioni abbiamo effettuato. Finché i < 3, ovvero i = 0,1,2
# viene ripetuto il corpo del ciclo while. Al termine di ogni iterazione dobbiamo incrementare la variabile contatore
# di 1. Se questo non viene fatto la condizione i < 3 resterà sempre vera, e quindi non usciremo mai dal while,
# eseguendo infinite ripetizioni.
# Un altro metodo per uscire da un ciclo while è l'istruzione break. Quando essa viene eseguita "rompe" il ciclo e
# consente di uscire. Ad esempio vogliamo iterare all'infinito (con una condizione sempre vera) e uscire quando
# l'utente inserisce un numero maggiore di 5

while True:                                        # while True indica un ciclo che viene eseguito all'infinito
    num1 = int(input("Inserisci un numero: "))
    if num1 <= 5:
        print("Numero inserito minore o uguale a 5")
    if num1 > 5:
        break

print("Sono uscito dal while")

# Così come per gli if, è possibile annidare più cicli while uno dentro l'altro. In questo caso il break esce solo dal
# ciclo più interno nel quale si trova, non consente di uscire da tutti i cicli. Dunque con 3 cicli while annidati
# sarà necessario usare 3 break per tornare nel livello più esterno.
# Esiste poi l'istruzione "continue" che consente, quando eseguita, di passare direttamente alla prossima iterazione
# del ciclo.

while True:
    num1 = int(input("Inserisci un numero: "))
    if num1 <= 5:
        continue
    if num1 > 5:
        break

# in questo caso quando si inserisce un numero <= 5 si passa direttamente alla prossima iterazione e tutte le eventuali
# istruzioni successive non vengono eseguite
