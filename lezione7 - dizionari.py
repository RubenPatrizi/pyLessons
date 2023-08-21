# I dizionari sono strutture dati che associano a una chiave un certo valore. Le chiavi di un dizionario devono
# essere univoche, mentre non ci sono vincoli sul valore. Per inizializzare un dizionario si può usare la
# funzione dict() che restituisce un dizionario vuoto, oppure utilizzare la notazione con parentesi graffe

diz = dict()
#OPPURE
diz = {}

# Possiamo anche inizializzare il dizionario con delle coppie chiave:valore già presenti, attraverso la sintassi
# chiave:valore. Ad esempio vogliamo creare un dizionario che associa a ciascuno studente il suo colore preferito

colori_preferiti = {
    "Richard": "blu",
    "Jane": "giallo",
    "Steve": "blu",
    "Brady": "verde",
    "John": "nero",
    "Leo": "rosso",
    "Frank": "bianco",
}

# Possiamo accedere ai dati di un dizionario mediante il metodo get, al quale dobbiamo passare una chiave. Il metodo
# ci ritornerà il valore associato a quella chiave. Ad esempio

print(colori_preferiti.get("Frank"))

# Se invece vogliamo aggiungere nuovi dati al dizionario dobbiamo semplicemente specificare un valore indicando
# una chiave tra parentesi quadre

colori_preferiti["Leo"] = "nero"

# In questo esempio la chiave "Leo" era già presente nel dizionario, quindi anziché aggiungere una coppia chiave:valore
# stiamo aggiornando il valore precedentemente memorizzato.
#
# Se invece vogliamo rimuovere una coppia dal dizionario basterà usare il metodo pop() indicando la chiave da eliminare

colori_preferiti.pop("Brady")

# Possiamo poi utilizzare i metodi keys() e values() per ottenere degli oggetti contenenti tutte le chiavi o tutti
# i valori del dizionario. Questi metodi tornano utili quando bisogna iterare sui dati con un ciclo for ad esempio
#
#
# ESERCIZIO
# Ripetere l'esercizio delle liste del calcolo della media dei voti con la differenza che questa volta i dati
# sono memorizzati in un dizionario: ad ogni studente (chiave) è associata una lista di voti. Infine memorizzare
# i risultati in un nuovo dizionario che associa a ciascuno studente la sua media e visualizzarla.

classe = {
    "Richard": [7,8,5,6,4,5,5],
    "Jane": [4,6,5,8,5,9,5],
    "Steve": [5,7,7,6,9,6],
    "Brady": [6,8,7,8,8,5],
    "John": [7,4,5,5,6,5],
    "Leo": [4,3,5,7,5,6],
    "Frank": [8,6,5,7,8,5]
}

