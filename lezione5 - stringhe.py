# Prendiamoci adesso una pausa dagli argomenti principali per approfondire l'utilizzo delle stringhe.
# Come abbiamo già detto una stringa può essere vista come un vettore/lista di caratteri, infatti "eredita"
# anche le proprietà delle liste, come ad esempio la possibilità di accedere direttamente alle singole posizioni,
# appendere altri elementi in fondo alla stringa, tagliarla, ecc.
# Tutti i metodi (funzioni) relative alle stringhe possono essere utilizzati mediante la 'dot notation', ovvero si
# inserisce un punto dopo il nome della variabile contenente la stringa

stringa = "python"
stringa              # provare a inserire un punto per far apparire l'elenco di metodi compatibili

# Come vediamo sono molto numerosi e sarebbe impossibile spiegarli tutti qui! Ci limitiamo quindi a mostrarne
# solo alcuni...

stringa.upper()   # converte la stringa in maiuscolo
stringa.count("py")     # conta il numero di occorrenze della sottostringa fornita (in questo caso "py")
stringa.index("th")     # ritorna l'indice al quale si trova la sottostringa fornita (in questo caso 2)
#                                                                                                   ^^^
#                                                                                                ATTENZIONE
#                                                                                       In Python, così come altri linguaggi,
#                                                                                       il primo indice di una stringa è 0,
#                                                                                       non 1. Ad esempio in "p y t h o n" gli indici
#                                                                                       dei caratteri saranno 0 1 2 3 4 5
#
stringa.isalpha()   # ritorna un valore booleano True se la stringa è formata solo da lettere
stringa.isnumeric()   # ritorna True se la stringa è formata solo da caratteri numerici
# e in generale tutti i metodi "is" ritornano un valore vero/falso
#
# Per conoscere il funzionamento in dettaglio di tutti i metodi la cosa migliore è, ovviamente, leggere la documentazione.
# Sappiamo che nessuno legge la documentazione ed è praticamente un meme, tuttavia è MOLTO importante andare a cercare
# come funzionano i vari metodi quando questi ci servono :)
# Documentazione stringhe -> https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# Vediamo ora come "tagliare" una stringa
# Ad esempio vogliamo eliminare i primi due caratteri dalla nostra stringa. La sintassi che si usa è la stessa usata
# per le liste/vettori, ovvero si utilizza la notazione con le parentesi quadre: ad esempio stringa[inizio:fine] vuol
# dire che stiamo selezionando una sottostringa della stringa principale che inizia nella posizione "inizio" e termina
# nella posizione precedente a "fine". Se vogliamo indicare "dall'inizio fino a" oppure "da... fino al termine"
# non si inseriscono gli indici corrispondendi a inizio/fine, ad esempio stringa[2:] vuol dire che stiamo selezionando
# la sottostringa che inizia dalla posizione 2 e termina dove termina la stringa originale.

stringa = "python"
stringa[2:]         # è la stringa "thon"
stringa[:-1]        # è la stringa "pytho"    <- le posizioni intese 'dalla fine' si indicano con indice NEGATIVO
stringa[3:5]        # è la stringa "ho"

# Ricordiamo poi che la concatenazione di più stringhe si esegue mediante l'operatore +, come se fosse una somma

str2 = "Java"
print(str2 + stringa[2:])       # stampa "Javathon"



# ESERCIZIO
# Scrivere un programma che chieda continuamente all'utente di inserire una stringa e si comporti nel seguente modo:
# - se la stringa inserita contiene almeno un carattere numerico stampare un messaggio di errore
# - se la stringa è "end" il programma termina
# - se la stringa è "append" il programma chiede altre due stringhe e le stampa una di seguito all'altra
# - se la stringa è "remove" il programma chiede altre due stringhe ed elimina dalla prima tutte le occorrenze della
#   seconda (ad esempio se la prima è "telefono" e la seconda è "fo" il programma deve stampare "teleno", mentre se
#   la seconda è "e" il risultato sarà "tlfono")
# - se la stringa è "count" il programma deve chiedere una stringa e contare il numero di occorrenze di ciascun
#   carattere che la compone. Ad esempio se si inserisce "scrivania" il programma dovrà stampare s: 1
#                                                                                                c: 1
#                                                                                                r: 1
#                                                                                                i: 2
#                                                                                                v: 1
#                                                                                                a: 2
#                                                                                                n: 1
