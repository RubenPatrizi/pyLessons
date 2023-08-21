classe = [
    ["Richard",7,8,5,6,4,5,5],      
    ["Jane",4,6,5,8,5,9,5],         
    ["Steve",5,7,7,6,9,6],          
    ["Brady",6,8,7,8,8,5],
    ["John",7,4,5,5,6,5],
    ["Leo",4,3,5,7,5,6],
    ["Frank",8,6,5,7,8,5],
]

somma = 0
media = 0
count = 0
name = ""
somma_classe = 0
count_classe = 0

for studente in classe:
    for element in studente:
        if isinstance(element,str):     # se è una stringa allora è il nome
            name = element
        else:                           # altrimenti è un voto
            somma += element
            count += 1
            somma_classe += element
            count_classe += 1
    media = somma / count              # calcolo media
    print(name, "->", "%.2f" % media)
    somma = count = 0                  # resetto somma e numero voti dello studente

print("\nMedia classe -> %.2f" % (somma_classe/count_classe))
