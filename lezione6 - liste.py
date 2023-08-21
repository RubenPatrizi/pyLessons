# Introduciamo ora una delle strutture dati più utili, le liste. Una lista non è altro che una sequenza di elementi
# che possono essere acceduti mediante indice usando la notazione con parentesi quadre, esattamente come già visto
# per le stringhe. In una lista possiamo rimuovere elementi, aggiungerli, iterare ecc. Importante sottolineare che
# gli elementi che compongono una lista possono essere di tipi diversi, tuttavia per evitare confusione è meglio
# che una lista contenga un solo tipo di elementi
#
# Per creare una lista abbiamo due opzioni: utilizzare la funzione list() che restituisce una lista vuota, oppure
# indicare gli elementi che compongono la lista tra parentesi quadre e separati da una virgola

lista = list()        # lista vuota
# OPPURE
lista = [3, 5, 2]     # lista contenente gli elementi 3, 5, 2

# Una volta creata la nostra lista possiamo eseguire una serie di operazioni su di essa. Così come per le stringhe
# tutti i possibili metodi compaiono usando la dot notation, cioè inserendo un punto dopo il nome della lista.
# Ad esempio per aggiungere elementi in fondo alla lista si utilizza il metodo append(elemento_da_aggiungere):

lista.append(3)
lista.append(1)
print(lista)        # stampando la lista osserviamo che adesso contiene [3,5,2,3,1]

# Per eliminare un elemento si usa invece il metodo remove(). ATTENZIONE -> remove() elimina solo la prima occorrenza
# dell'elemento specificato. Se in questo caso scrivessimo
lista.remove(3)
print(lista)
# osserviamo che solo il 3 all'inizio della lista è stato eliminato, mentre quello in penultima posizione è
# ancora presente.
#
# Esistono poi i metodi pop() e insert(), che equivalgono a remove() e append() con la differenza che essi consentono
# di inserire e rimuovere in posizioni specifiche della lista

lista.pop(0)      # elimina l'elemento con indice 0, ovvero il primo elemento, in questo caso 5
lista.insert(2,10)       # inserisce in posizione 2 l'elemento 10
print(lista)

# Importante notare che quando si inserisce o rimuove un elemento in mezzo alla lista tutti gli elementi successivi
# verranno spostati avanti o indietro di una posizione
#
# Possiamo infine ordinare gli elementi di una lista mediante il metodo sort()
# Proviamo a ordinare la nostra lista

lista.sort()
print(lista)

# Altri metodi consentono di fondere due liste, copiarle, invertirle ecc. ma sono piuttosto semplici da capire.
#
# IMPORTANTE -> per fare una copia di una lista BISOGNA usare il metodo apposito, NON creare una nuova lista e porla
# uguale alla lista che vogliamo copiare, in questo modo stiamo solo copiando il riferimento alla lista, ma i dati
# in memoria saranno gli stessi. Esempio per chiarire:

nuova_lista = lista       # SBAGLIATO -> non abbiamo fatto una copia della lista, abbiamo solo creato un nuovo
#                                        riferimento che punta agli stessi dati della lista vecchia. Se facciamo
#                                        una modifica su nuova_lista questa avrà effetto anche sulla lista originale

nuova_lista.pop(-1)      # eliminiamo l'ultimo elemento da nuova_lista
print(lista)             # stampando la vecchia lista osserviamo che 10 è stato rimosso anche da qui


nuova_lista = lista.copy()   # CORRETTO -> abbiamo fatto una copia della lista, adesso in memoria esistono due
#                                          liste composte dagli stessi elementi ma indipendenti tra loro

nuova_lista.append(5)
print("Nuova lista: ", nuova_lista, "\nVecchia lista: ", lista)

# In questo caso la modifica è avvenuta solo sulla nuova lista, come ci aspettiamo.
#
# Se vogliamo analizzare gli elementi di una lista è conveniente utilizzare un ciclo for, così come già visto
# per le stringhe

for num in lista:
    print(num**2)      # stampa il quadrato di ogni numero nella lista



# Cosa succede però se gli elementi che compongono una lista sono a loro volta liste? In questo caso abbiamo a che
# fare con una matrice, ovvero una struttura 2D caratterizzata da righe e colonne (non è obbligatorio che le liste
# siano tutte della stessa lunghezza).
# Per accedere a un elemento di una matrice dobbiamo specificare entrambi gli indici di quell'elemento utilizzando
# due coppie di parentesi quadre

matrice = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]       # creiamo una matrice con 3 righe, ovvero composta da 3 liste
print(matrice)

# Per accedere a un elemento della matrice dovremo usare due parentesi quadre specificando indici di riga e colonna

print(matrice[0][0])     # stampa il primo elemento della matrice, ovvero 0
print(matrice[1][3])     # stampa l'elemento di riga 1 e colonna 3, ovvero 7

# Per scandire gli elementi di una matrice dovremo utilizzare due cicli for annidati

for riga in matrice:        # la variabile riga è, ad ogni iterazione, una delle liste che compongono la matrice
    for num in riga:        # il secondo ciclo for serve a scandire ogni lista
        print("m", num)

# Importante notare che se eseguiamo remove() o pop() su di una matrice stiamo rimuovendo una lista, ovvero un'intera
# riga. Se vogliamo eliminare un elemento specifico bisogna accedere alla lista che lo contiene ed eseguire la
# rimozione su di essa

matrice[2].remove(10)      # rimuovo il valore 10 dalla riga di indice 2
print(matrice[2])          # il 10 è stato rimosso

# Per quanto riguarda l'inserimento di righe valgono le stesse considerazioni fatte per le liste normali:
# inserire una riga in una certa posizione comporta lo spostamento in avanti di tutte le righe successive, così
# come rimuoverla comporta lo spostamento indietro di tutte le righe successive.
# Il concetto fondamentale quindi è che in una lista non possono esserci posizioni vuote. Se proprio abbiamo bisogno
# di avere degli spazi vuoti possiamo utilizzare dei valori speciali che quando letti interpretiamo come posizioni vuote
#
print("-"*15)
#
# ESERCIZIO
# Viene data una matrice in cui le righe contengono in prima posizione il nome di uno studente e nelle posizioni
# successive i suoi voti. Per ogni studente stampare il suo nome seguito dalla media dei suoi voti. Stampare infine
# anche la media voti della classe
#
# Soluzione esercizio -> https://github.com/SSSwordsman/pyLessons/blob/master/classe_soluzione.py

classe = [
    ["Richard",7,8,5,6,4,5,5],           # ad esempio per la prima riga vogliamo stampare "Richard -> 5.71"
    ["Jane",4,6,5,8,5,9,5],              # NOTA: per stampare solo due cifre decimali usare la notazione "%.2f" % media
    ["Steve",5,7,7,6,9,6],               #       dove ad esempio media è la variabile che contiene la media dello studente
    ["Brady",6,8,7,8,8,5],
    ["John",7,4,5,5,6,5],                # Per verificare se un elemento è una stringa o un intero utilizzare la funzione
    ["Leo",4,3,5,7,5,6],                 # isinstance(variabile,tipo), cioè ad esempio isinstance(elemento,str) oppure
    ["Frank",8,6,5,7,8,5],               # isinstance(elemento,int) dove elemento è un elemento della matrice
]
