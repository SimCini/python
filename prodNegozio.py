def prezzo_medio(prezzi_prodotti, prodotto, giorno):
    c=0
    sommaPrezzi=0
    for prodotti,giorni,prezzi in prezzi_prodotti:
        if (giorni==giorno and prodotti==prodotto):
            c+=1
            sommaPrezzi+=prezzi
    if c>0:
        media = sommaPrezzi/c
        return media
    else:
        return("Prodotto inesistente")


prezzi_prodotti = (
    ("Mela", "Lunedì", 1.0),
    ("Mela", "Martedì", 1.2),
    ("Mela", "Mercoledì", 1.1),
    ("Banana", "Lunedì", 0.8),
    ("Banana", "Martedì", 0.9),
    ("Banana", "Mercoledì", 0.7),
)

nomeProd = input("Inserisci prodotto da controllare: ")
giorno = input("Inserisci giorno della settimana: ")
print(f"Il prezzo medio del prodotto {nomeProd} è: ",prezzo_medio(prezzi_prodotti, nomeProd, giorno))