# I cicli for in Python sono diversi dai cicli for presenti in altri linguaggi come C o Java, dove vengono usati per
# eseguire delle istruzioni un certo numero di volte. Anche in Python è possibile usarli in questo modo, tuttavia
# la loro vera utilità è che consentono di scandire uno per uno gli elementi di strutture dati complesse come liste
# o dizionari.
# Per ora concentriamoci sull'utilizzo classico: per eseguire il corpo del for un certo numero di volte si usa la
# seguente sintassi

for contatore in range(0,10):
    print(contatore)

# dichiariamo quindi una variabile (qui chiamata contatore ma che può avere un nome qualsiasi) e successivamente
# la parola chiave "in" seguita dalla funzione range(inizio,fine). In questo caso il primo valore assunto dal contatore
# sarà 0, alla successiva iterazione sarà 1 e così via finché non diventa pari a 10 e si esce dal ciclo for.
# Chiaramente possiamo modificare il valore del contatore all'interno del ciclo, dunque, così come per il while,
# è bene assicurarsi di non rimanere intrappolati all'interno del ciclo.
#
# Per il momento non abbiamo ancora parlato di liste e dizionari, tuttavia possiamo ottenere lo stesso comportamento
# che avremmo con queste strutture dati utilizzando una stringa.
# Se ad esempio scriviamo

for carattere in "Hello":
    print(carattere)

# avremo che ad ogni iterazione la variabile carattere assume il valore di uno dei caratteri che compongono la stringa,
# in ordine da quello iniziale (più a sinistra) a quello finale (più a destra).
# Se al posto di una stringa avessimo avuto una lista il comportamento sarebbe stato del tutto equivalente: ad ogni
# iterazione la variabile assume il valore di un elemento della lista.
#
# Anche nei cicli for è possibile utilizzare il costrutto break per terminare il ciclo anticipatamente

for carattere in "Hello":
    if carattere == "e":
        break
    print(carattere)

# Anche in questo caso è possibile inserire cicli for annidati, osservando le stesse regole già descritte per i cicli
# while. Lo stesso vale per l'istruzione continue.
