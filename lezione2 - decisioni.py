# Nella lezione 1 abbiamo introdotto le variabili e le principali operazioni aritmetiche.
# Prima di proseguire parliamo brevemente del fatto che in Python anche le stringhe supportano alcune operazioni
#               + concatenazione
#               * ripetizione
# ad esempio possiamo stampare più stringhe una di seguito all'altra "sommandole"

print("stringa 1\n" + "stringa 2\n" + "stringa 3")  # il \n è un carattere speciale che consente di andare a capo

# oppure possiamo scegliere di ripetere una stringa un certo numero di volte

print("-" * 15 + "\nCAPITOLO 2: DECISIONI")

# Durante l'esecuzione di un programma potremmo voler prendere strade diverse a seconda dei risultati ottenuti
# da operazioni precedenti. Ad esempio vogliamo stampare una certa stringa se il numero scritto dall'utente
# è maggiore di 5 oppure un'altra stringa se è minore. Le decisioni in Python avvengono mediante la parola
# chiave if, seguita dalla condizione che vogliamo verificare e dal carattere di due punti

num1 = int(input("Inserisci un numero: "))    # ho inserito l'input direttamente all'interno dell'int in modo che il
                                              # risultato venga direttamente convertito senza scrivere due righe separate
if num1 > 5:
    print("Il numero è maggiore di 5")

# Dopo aver premuto invio notiamo che vengono automaticamente lasciati 4 spazi dall'inizio della riga (ovvero un carattere
# di tabulazione (il tasto TAB)). Questo perché Python utilizza l'indentazione del testo per capire quali sono i diversi
# rami di esecuzione del programma, il corpo dei cicli e delle funzioni (che vedremo più avanti). In pratica se la condizione
# dell'if è verificata il programma eseguirà tutte le istruzioni successive che si trovano a un TAB dal margine sinistro.
# Per tornare al flusso di esecuzione "principale" del programma basterà tornare a scrivere al margine sinistro

if True:                         # True e False sono i valori booleani utilizzabili in Python, if True vuol dire che
    print("\nEntro nell'if")     # si entra sempre nel ramo dell'if perché la condizione è sempre verificata
print("Esco dall'if\n")

# Insieme all'if troviamo poi la parola chiave else, cioè "altrimenti" in inglese. Quando dopo l'if troviamo anche un else
# il programma funziona nel seguente modo: se la condizione specificata nell'if è verificata viene eseguito il ramo
# corrispondente, altrimenti viene eseguito il ramo dell'else

if num1 > 5:
    print("Il numero è maggiore di 5")
else:
    print("Il numero è minore o uguale a 5")

# Potrebbe servirci però di entrare nell'else solo se è verificata un'altra condizione. Utilizziamo quindi la parola
# chiave elif (ovvero "else if"). Se la condizione dell'if non è verificata viene controllata quella specificata
# nell'elif (possiamo scrivere più di un elif per creare più rami decisionali). Dopo gli elif è possibile scrivere
# un else, in cui si entra se nessuna delle condizioni precedenti è verificata.

num1 = int(input("Inserisci un numero: "))

if num1 > 7:
    print("Il numero è maggiore di 7")
elif num1 == 3:
    print("Il numero è 3")
elif num1 == 0:
    print("Il numero è 0")
else:
    print("Il numero è minore o uguale a 7 ma diverso da 0 e 3")

# Notiamo che per verificare un'uguaglianza bisogna utilizzare l'espressione == (il singolo = è usato per assegnare i
# valori alle variabili come abbiamo già visto). Le principali condizioni che possiamo verificare sono:
#                      >   maggiore
#                      <   minore
#                      >=  maggiore o uguale
#                      <=  minore o uguale
#                      ==  uguale
#                      !=  diverso
# Possiamo anche verificare più condizioni contemporaneamente attraverso i seguenti operatori logici
#                      and   entrambe le condizioni devono essere vere
#                      or   è sufficiente che almeno una delle condizioni sia vera
#                      not   nega una condizione
# Ad esempio vogliamo verificare che un numero sia compreso tra 3 e 6

num1 = int(input("Inserisci un numero: "))
if num1 > 3 and num1 < 6:
    print("Il numero è compreso tra 3 e 6")

# Altro esempio

if num1 != 3 or num1 <= 6:
    print("Il numero è diverso da 3 OPPURE è minore o uguale a 6")

# Come facciamo però per verificare che il numero non sia compreso tra 3 e 6?
# Se scrivessimo

if not num1 >= 3 and num1 <= 6:
    print("\n")
    # entreremmo nell'if se il numero è MINORE di 3 (l'opposto di >=) e contemporaneamente minore o uguale a 6, ovvero
    # solo quando il numero è più piccolo di 3, perché il not agisce solo sulla condizione scritta dopo di esso
# Per ottenere il comportamento desiderato dobbiamo negare entrambe le condizioni, ovvero scrivere

if not num1 >= 3 and not num1 <= 6:
    print("Il numero NON è compreso tra 3 e 6")

# Oppure più brevemente

if not (num1 >= 3 and num1 <= 6):
    print("Il numero NON è compreso tra 3 e 6")

# Infine diciamo che è possibile scrivere degli if "annidati", ovvero uno dentro l'altro (non c'è un limite a quanti if
# possiamo annidare, ma è bene non usarne più di 2 o 3 perché il comportamento del nostro programma può diventare
# molto difficile da capire per chi legge)

num1 = int(input("Inserisci un numero: "))

if num1 > 3:
    print("Numero maggiore di 3")
    if num1 < 7:
        print("Numero compreso tra 3 e 7")
    else:
        print("Numero maggiore di 7")

# In questi esempi abbiamo utilizzato solo numeri ma ovviamente è possibile anche fare confronti tra stringhe

string1 = input("Inserisci una stringa: ")
if string1 == "neve":
    print("❄")


print("-"*15)

# ESERCIZIO
# Scrivere un programma in grado di calcolare le soluzioni di un'equazione di secondo grado del tipo a*x^2 + b*x + c = 0.
# In particolare il programma deve prima chiedere all'utente il valore dei parametri a, b, c e successivamente far
# scegliere all'utente se vuole che venga stampato il tipo o il valore delle soluzioni (ad esempio scrivendo la stringa
# "tipo" oppure "valore"). A questo punto bisogna stampare il tipo delle soluzioni in base al delta (reali e distinte,
# reali e coincidenti, complesse e coniugate) oppure il loro valore (usando la classica formula per le equazioni
# di secondo grado). Calcolare il valore solo nel caso in cui le soluzioni NON siano complesse (delta < 0).
# Formula per il delta -> https://wikimedia.org/api/rest_v1/media/math/render/svg/bb8e9a3f8c6c4c62de207ffb8a59ea17c0584932
# Formula risolutiva -> https://wikimedia.org/api/rest_v1/media/math/render/svg/00c22777378f9c594c71158fea8946f2495f2a28
# Per aprire i link cliccare mentre si tiene premuto il tasto Ctrl
# Per calcolare la radice quadrata usare la funzione sqrt()


from math import sqrt     # importo la funzione sqrt (vedremo meglio le importazioni più avanti)
# completare l'esercizio qui sotto

