# Ciao! Benvenuto in questo corso di Python!

# Probabilmente avrai già sentito parlare di questo linguaggio di programmazione,
# infatti Python è da parecchio tempo il linguaggio più utilizzato al mondo.
# Uno dei motivi della sua diffusione è sicuramente la sua sintassi molto snella
# e semplice da imparare anche per chi si approccia al mondo della programmazione per la prima volta.
# Niente ; a ogni riga o colonne interminabili di parentesi graffe!  :D


# Iniziamo a vedere qualche esempio di programma Python con il canonico "Hello world"
# Per stampare qualcosa sullo schermo in Python si utilizza la funzione print

print("Hello world")

# Eseguendo questa istruzione "Hello world" verrà stampata sullo schermo
# Come per gli altri linguaggi, anche in Python i parametri delle funzioni vanno passati tra parentesi tonde.
# In questo caso utilizziamo le virgolette poiché vogliamo stampare una stringa, ovvero una sequenza di caratteri.
# Approfittiamo per introdurre il concetto di VARIABILE:
# Possiamo vedere una variabile come un contenitore, una porzione di memoria nella quale memorizziamo dei dati.
# Inizializziamo una variabile con la seguente sintassi:

variabile = "valore"       # il nome da assegnare alla variabile possiamo sceglierlo a piacere

# Abbiamo creato una variabile dal nome 'variabile' il cui contenuto è la stringa "valore".
# Da questo momento in poi qualunque volta scriveremo variabile nel nostro programma sarà
# come se stessimo scrivendo il suo contenuto.
# Per cui se ad esempio scrivessimo

print(variabile)

# verrà stampata la stringa "valore" (notare che questa volta non abbiamo utilizzato le virgolette
# perché le variabili vanno richiamate attraverso il nome esatto con cui sono state dichiarate).
# "Ok bello, ma se volessi stampare altro oltre alle stringhe?"
# Naturalmente ci sono altri tipi di dati oltre alle stringhe, ovvero:
# -int
#  numeri interi, sia positivi che negativi
#
# -float
#  numeri decimali (con il punto)
#
# -boolean
#  un valore che può essere vero o falso (utile per fare controlli e decisioni)
#
# Python non è un linguaggio fortemente tipizzato come C o Java, cioè quando si dichiara una variabile
# non bisogna specificarne il tipo e il suo valore può essere cambiato dinamicamente durante
# l'esecuzione del programma. Ad esempio:

variabile = 3

# 'variabile' conteneva la stringa "valore", ma da questa istruzione in poi essa conterrà il numero intero 3
# Se adesso ripetessimo il print otterremmo la stampa del valore 3


# Passiamo ora a qualcosa di più interessante: operazioni aritmetiche  :D
# Possiamo effettuare operazioni tra numeri attraverso simboli particolari
#       + somma
#       - differenza
#       * prodotto
#       / quoziente
#       % resto
#       ** elevamento a potenza
# Ad esempio possiamo scrivere:

num1 = 2
num2 = 5
risultato = num1 + num2
print(risultato)        # potremmo anche scrivere direttamente print(num1+num2) senza utilizzare una terza variabile intermedia

# Per rendere le cose più interattive parliamo della funzione input(). Questa funzione permette di leggere valori
# inseriti dall'utente mediante la tastiera

stringa1 = input("Inserisci il primo numero: ")
stringa2 = input("Inserisci il secondo numero: ")
risultato = int(stringa1) + int(stringa2)
print("La somma è %d" % risultato)

# Ok, è un bel po' di roba nuova, vediamo di spiegarla per bene!
# La funzione input riceve una stringa da visualizzare sulla console e restituisce il valore inserito dall'utente sotto
# forma di stringa (se il primo numero che inseriamo è 5, il valore letto sarà la stringa "5", non il numero 5).
# Questo è il motivo per il quale per calcolare il risultato dobbiamo prima effettuare una CONVERSIONE del valore appena letto
# mediante la funzione int(). Naturalmente possiamo anche fare l'opposto e convertire un numero in stringa, mediante
# la funzione str().
# Abbiamo imparato a stampare delle stringhe dal contenuto statico, ovvero che non cambia mai, come facciamo però se
# vogliamo stampare un valore che cambia dinamicamente in base ai valori inseriti dall`utente?
# Dobbiamo utilizzare i seguenti caratteri speciali (i principali, ma ce ne sono molti altri):
#            %d per gli interi
#            %f per i float
#            %s per le stringhe
# e dopo il termine della stringa (dopo le virgolette) dobbiamo inserire il carattere % seguito dal valore che vogliamo
# sostituire all'interno della stringa. Se abbiamo più valori da stampare nella stessa espressione basterà scrivere
# tutti gli elementi dopo il % separati da una virgola e all'interno di una coppia di parentesi tonde. Ad esempio:

num1 = int(stringa1)
num2 = int(stringa2)
print("La somma di %d e %d vale %d" % (num1,num2,risultato))

# In alternativa possiamo utilizzare un altro metodo particolare: si inserisce il carattere f minuscolo PRIMA delle
# virgolette di apertura della stringa e successivamente i valori che vogliamo sostituire andranno inseriti direttamente
# all'interno della stringa stessa e in una coppia di parentesi graffe

print(f"La somma di {num1} e {num2} vale {risultato}")

# Queste due istruzioni sono del tutto equivalenti, tuttavia osserviamo che il metodo f è più leggibile.


print("----------------------------")

# ESERCIZIO
# Scrivere un programma in grado di calcolare l'area di un trapezio isoscele. I dati devono essere inseriti dall'utente
# e il risultato deve poi essere visualizzato sullo schermo
#
