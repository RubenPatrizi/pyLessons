classe = {
    "Richard": [7,8,5,6,4,5,5],
    "Jane": [4,6,5,8,5,9,5],
    "Steve": [5,7,7,6,9,6],
    "Brady": [6,8,7,8,8,5],
    "John": [7,4,5,5,6,5],
    "Leo": [4,3,5,7,5,6],
    "Frank": [8,6,5,7,8,5]
}

somma = 0
count = 0
somma_totale = 0
count_totale = 0
media_per_studente = {}

for chiave in classe:
    for num in classe.get(chiave):
        somma += num
        count += 1
        somma_totale += num
    count_totale += len(classe[chiave])
    print(chiave + " -> %.2f" % (somma/count))
    media_per_studente[chiave] = somma/count
    somma = count = 0

print("\nMedia classe -> %.2f\n" % (somma_totale/count_totale))

print(media_per_studente)
