while True:
    comando = input("\nScegli un comando:\n"
                    "end -> esci\n"
                    "append -> concatena due stringhe\n"
                    "remove -> rimuovi sottostringa\n"
                    "count -> conta lettere\n")
    if not comando.isalpha():
        print("Il comando non può contenere numeri\n")
    elif comando == "end":
        break
    elif comando == "append":
        stringa1 = input("Inserisci la prima stringa: ")
        stringa2 = input("Inserisci la seconda stringa: ")
        print("Risultato: " + stringa1 + stringa2)
    elif comando == "remove":
        stringa1 = input("Inserisci una stringa: ")
        da_rimuovere = input("Inserisci la stringa da rimuovere: ")
        risultato = stringa1.replace(da_rimuovere,"")             # rimpiazzo le occorrenze della sottostringa da rimuovere
        print("Risultato: " + risultato)                                # con la stringa vuota "", di fatto eliminandole
    elif comando == "count":
        stringa1 = input("Inserisci una stringa: ")
        for char in stringa1:
            count = stringa1.count(char)
            if count == 0:                         # se non ci sono più occorrenze del carattere è perché si tratta di un
                continue                           # carattere che abbiamo già incontrato, dunque saltiamo al prossimo
            print(char + ": %d" % count)
            if count > 1:                                         # se ci sono più occorrenze del carattere allora lo rimuoviamo
                stringa1 = stringa1.replace(char, "")      # dalla stringa, in modo da non incontrarlo nuovamente
    else:
        print("Comando errato\n")
